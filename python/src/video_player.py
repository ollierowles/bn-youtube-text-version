"""A video player class."""
import random

from video_library import VideoLibrary


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self.video_library = VideoLibrary()
        self.status_codes = {}
        self.status_codes['current_video_id'] = ''
        self.status_codes['is_playing'] = False
        self.status_codes['is_paused'] = True


    def number_of_videos(self):
        num_videos = len(self.video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        all_videos = self.video_library.get_all_videos()
        sorted_videos = sorted(all_videos, key=lambda x: x.title)
        print("Here's a list of all available videos:")

        for i in sorted_videos:
            title_txt = str(i.title)
            video_id_txt = "(" + str(i.video_id) + ")"
            tag_txt = "[" + " ".join(i.tags) + "]"
            print(f"{title_txt} {video_id_txt} {tag_txt}")

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """

        if self.status_codes['is_playing'] is True:
            self.stop_video()

        current_video = self.video_library.get_video(video_id)
        self.status_codes['current_video_id'] = self.video_library.get_video(video_id)
        self.status_codes['is_paused'] = False

        if not current_video:
            print("Cannot play video: Video does not exist")
            return

        if self.status_codes['is_playing'] is True:
            print(f"Playing video: {current_video.title}")

        print(f"Playing video: {current_video.title}")
        self.status_codes['is_playing'] = True


    def stop_video(self):
        """Stops the current video."""
        if self.status_codes['is_playing']:
            print(f"Stopping video: {self.status_codes['current_video_id'].title}")
            self.status_codes['is_playing'] = False
        else:
            print('Cannot stop video: No video is currently playing')


    def play_random_video(self):
        """Plays a random video from the video library."""
        all_videos = self.video_library.get_all_videos()

        if self.status_codes['is_playing']:
            self.stop_video(self.status_codes['current_video_id'])

        random_video = random.choice(all_videos)
        self.play_video(random_video.video_id)

    def pause_video(self):
        """Pauses the current video."""
        if not self.status_codes['is_paused']:
            print(f"Pausing video: {self.status_codes['current_video_id'].title}")
            self.status_codes['is_paused'] = True
        else:
            print(f"Video already paused: {self.status_codes['current_video_id'].title}")

    def continue_video(self):
        """Resumes playing the current video."""

        if not self.status_codes['is_playing']:
            print(f"Cannot continue video: No video is currently playing")
            return

        if self.status_codes['is_paused']:
            print(f"Continuing video: {self.status_codes['current_video_id'].title}")
            self.status_codes['is_paused'] = False
        else:
            print(f"Cannot continue video: Video is not paused")


    def show_playing(self):
        """Displays video currently playing."""
        if not self.status_codes['is_paused']:
            print(f"Currently playing: {self.status_codes['current_video_id'].title} {self.status_codes['current_video_id'].video_id} [{self.status_codes['current_video_id'].tags}]")
        else:
            print(f"No video is currently playing")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
