from unittest import TestCase

from Video import Video


class video(TestCase):

    def test_that_video_can_be_play(self):
        video = Video("Boys Before Flower", 30, 12)
        self.assertEqual(video.play(), "Boys Before Flower is now playing")

    def test_for_video_minute(self):
        video = Video("Boys Before Flower", 30, 12)
        self.assertEqual(video.advance_minutes(),"30 minutes")

    def test_for_video_is_finished(self):
        video = Video("Boys Before Flower", 30, 30)
        video.duration =30
        video.current_position =30

        self.assertTrue(video.is_finished())

    def test_for_video_to_restart(self ):
        video = Video("Boys Before Flower", 30, 30)
        video.duration =30
        video.current_position =30

        self.assertTrue(video.restart())

    def test_for_time_remaining(self):
        video = Video("Boys Before Flower", 30, 30)
        self.duration =30
        video.current_position =15
        self.assertEqual(video.time_remaining(),15)