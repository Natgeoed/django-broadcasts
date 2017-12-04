# import json
from datetime import timedelta

from django.test import TestCase

try:
    from django.utils.timezone import now
except ImportError:
    import datetime
    now = datetime.datetime.now

from broadcasts.models import BroadcastMessage


class BroadcastManagerTest(TestCase):
    """
    This test case ensures that the manager methods return the correct
    broadcast or broadcasts based on the start time, end time, and published
    status of the available messages.
    """

    def setUp(self):
        """
        The test case should have one broadcast message for each combination of
        setting, i.e. current, past, future, published, with or without start
        dates
        """

        today = now()
        yesterday = today - timedelta(days=1)
        tomorrow = today + timedelta(days=1)
        morefuture = today + timedelta(days=2)

        self.pub_expired = BroadcastMessage.objects.create(
            message="Expired messsage",
            end_time=yesterday,
        )
        self.pub_current_no_start = BroadcastMessage.objects.create(
            message="Current, but no start",
            end_time=morefuture,
        )
        self.pub_current_start_yesterday = BroadcastMessage.objects.create(
            message="Current, started yesterday",
            start_time=yesterday,
            end_time=tomorrow,
        )
        self.pub_current_ends_later = BroadcastMessage.objects.create(
            message="Current, ends later",
            start_time=yesterday,
            end_time=morefuture,
        )
        self.unpublished = BroadcastMessage.objects.create(
            message="Unpublished",
            start_time=yesterday,
            end_time=morefuture,
            is_published=False,
        )

    def test_past_broadcasts(self):
        """Ensure that expired broadcasts are not returned"""
        self.assertEqual(len(BroadcastMessage.objects.all()), 5)
        self.assertEqual(len(BroadcastMessage.objects.current()), 3)

    def test_latest_broadcast(self):
        """Ensure that the latest broadcast is soonest to expire, current"""
        self.assertEqual(
            self.pub_current_start_yesterday,
            BroadcastMessage.objects.latest()
        )

    def test_no_broadcasts(self):
        BroadcastMessage.objects.all().delete()
        self.assertEqual(BroadcastMessage.objects.latest(), None)

    def test_published_flag(self):
        self.assertEqual(BroadcastMessage.objects.active().count(), 4)

    # def test_ajax_messages(self):
    #     result = self.client.get('/messages/')
    #     objs = BroadcastMessage.objects.current().for_unauth_users()
    #     msgs = [x.msg_info() for x in objs]
    #     # ids = [x.id for x in objs]
    #     # res_ids = map(int, result.cookies['excluded_broadcasts'].value.split(","))
    #     self.assertEqual(json.loads(result.content), msgs)
    #     # self.assertEqual(set(res_ids), set(ids))
    #     new_result = self.client.get('/messages/', HTTP_COOKIE=result.cookies)
    #     # res_ids = map(int, new_result.cookies['excluded_broadcasts'].value.split(","))
    #     # self.assertEqual(set(res_ids), set(ids))
    #     self.assertEqual(new_result.content, "[]")

    # def test_message_paths(self):
    #     """
    #     First get / which should eliminate them when we get /items/
    #     """
    #     # Set up one to only work on a subpath
    #     self.pub_current_no_start.url_target = '/items/.*'
    #     self.pub_current_no_start.save()

    #     # Get root path, which should exclude it
    #     result = self.client.get('/messages/', HTTP_REFERER='/')
    #     objs = BroadcastMessage.objects.current().exclude(url_target='/items/.*')
    #     msgs = [x.msg_info() for x in objs]
    #     ids = [x.id for x in objs]
    #     res_ids = map(int, result.cookies['excluded_broadcasts'].value.split(","))
    #     self.assertEqual(json.loads(result.content), msgs)
    #     self.assertEqual(set(res_ids), set(ids))

    #     # Get the subpath, which should only show the single message
    #     new_result = self.client.get('/messages/', HTTP_REFERER='/items/', HTTP_COOKIE=result.cookies)
    #     res_ids = map(int, new_result.cookies['excluded_broadcasts'].value.split(","))
    #     objs = [self.pub_current_no_start]
    #     msgs = [x.msg_info() for x in objs]
    #     ids.append(self.pub_current_no_start.id)
    #     self.assertEqual(set(res_ids), set(ids))
    #     self.assertEqual(json.loads(new_result.content), msgs)

    #     # Get another subpath, which should show nothing
    #     new_result2 = self.client.get('/messages/', HTTP_REFERER='/items/1/', HTTP_COOKIE=new_result.cookies)
    #     res_ids = map(int, new_result2.cookies['excluded_broadcasts'].value.split(","))
    #     objs = []
    #     msgs = [{u'title': x.title, u'message': x.message} for x in objs]
    #     self.assertEqual(set(res_ids), set(ids))
    #     self.assertEqual(json.loads(new_result2.content), msgs)
