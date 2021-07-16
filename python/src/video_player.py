"""A video player class."""
import random

from video_library import VideoLibrary
from video_playlist import Playlist
from video_flags import Flagged



class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self.video_library = VideoLibrary()
        self.status_codes = {}
        self.playlists = {}
        self.flagged_videos = {}
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
            if i.video_id in self.flagged_videos:
                flag_txt = "- FLAGGED (reason: " + (self.flagged_videos[i.video_id].reason) + ")"
            else:
                flag_txt = ""
            print(f"{title_txt} {video_id_txt} {tag_txt} {flag_txt}")

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """

        if not self.video_library._videos.get(video_id, None):
            print("Cannot play video: Video does not exist")
            return

        if video_id in self.flagged_videos:
            if self.flagged_videos[video_id].status == True:
                print(f"Cannot play video: Video is currently flagged (reason: {self.flagged_videos[video_id].reason})")
                return

        if self.status_codes['is_playing'] is True and self.status_codes[
            'current_video_id'] in self.video_library.get_all_videos():
            self.stop_video()

        current_video = self.video_library.get_video(video_id)
        self.status_codes['current_video_id'] = self.video_library.get_video(video_id)
        self.status_codes['is_paused'] = False

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

        random_video = random.choice(all_videos)
        num_videos = len(all_videos)

        if random_video.video_id in self.flagged_videos:
            random_video = random.choice(all_videos)
            num_videos -= num_videos
            if num_videos == 0:
                print("No videos available")
                return

        if self.status_codes['is_playing']:
            self.stop_video()

        self.play_video(random_video.video_id)

    def pause_video(self):
        """Pauses the current video."""
        if not self.status_codes['current_video_id']:
            print("Cannot pause video: No video is currently playing")
            return

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
        if self.status_codes['is_playing']:
            title_txt = str(self.status_codes['current_video_id'].title)
            video_id_txt = "(" + str(self.status_codes['current_video_id'].video_id) + ")"
            tag_txt = "[" + " ".join(self.status_codes['current_video_id'].tags) + "]"
            if self.status_codes['is_paused']:
                put_paused = '- PAUSED'
            else:
                put_paused = ""
            print(f"Currently playing: {title_txt} {video_id_txt} {tag_txt} {put_paused}")
        else:
            print(f"No video is currently playing")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.lower() not in self.playlists:
            print(f"Successfully created new playlist: {playlist_name}")
            self.playlists[playlist_name.lower()] = Playlist(playlist_name)
        else:
            print("Cannot create playlist: A playlist with the same name already "
                  "exists")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        if playlist_name.lower() not in self.playlists:
            print(f"Cannot add video to {playlist_name}: Playlist does not exist")
            return

        if not self.video_library.videos.get(video_id, None):
            print(f"Cannot add video to {playlist_name}: Video does not exist")
            return

        if self.video_library.get_video(video_id) in self.playlists[playlist_name.lower()].videos:
            print(f"Cannot add video to {playlist_name}: Video already added")
            return

        if video_id in self.flagged_videos:
            print(f"Cannot add video to {playlist_name}: Video is currently flagged (reason: {self.flagged_videos[video_id].reason})")
            return

        print(f"Added video to {playlist_name}: {self.video_library.get_video(video_id).title}")
        self.playlists[playlist_name.lower()].videos.append(self.video_library.get_video(video_id))

    def show_all_playlists(self):
        """Display all playlists."""

        if len(self.playlists) == 0:
            print("No playlists exist yet")
            return

        print("Showing all playlists:")
        playlist_length = len(self.playlists)
        for p in sorted(self.playlists):
            print(f"{self.playlists[p].name}")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.lower() not in self.playlists:
            print(f"Cannot show playlist {playlist_name}: Playlist does not exist")
            return

        if len(self.playlists[playlist_name.lower()].videos) == 0:
            print(f"Showing playlist: {playlist_name}")
            print("No videos here yet")
            return

        print(f"Showing playlist: {playlist_name}")
        for v in self.playlists[playlist_name.lower()].videos:
            title_txt = str(v.title)
            video_id_txt = "(" + str(v.video_id) + ")"
            tag_txt = "[" + " ".join(v.tags) + "]"
            if v.video_id in self.flagged_videos:
                flag_txt = "- FLAGGED (reason: " + (self.flagged_videos[v.video_id].reason) + ")"
            else:
                flag_txt = ""
            print(f"{title_txt} {video_id_txt} {tag_txt} {flag_txt}")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        if playlist_name.lower() not in self.playlists:
            print(f"Cannot remove video from {playlist_name}: Playlist does not exist")
            return

        if not self.video_library.videos.get(video_id, None):
            print(f"Cannot remove video from {playlist_name}: Video does not exist")
            return

        if self.video_library.get_video(video_id) not in self.playlists[playlist_name.lower()].videos:
            print(f"Cannot remove video from {playlist_name}: Video is not in playlist")
            return

        print(f"Removed video from {playlist_name}: {self.video_library.get_video(video_id).title}")
        self.playlists[playlist_name.lower()].videos.remove(self.video_library.get_video(video_id))

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.lower() not in self.playlists:
            print(f"Cannot clear playlist {playlist_name}: Playlist does not exist")
            return
        print(f"Successfully removed all videos from {playlist_name}")
        self.playlists[playlist_name.lower()].videos = []

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.lower() not in self.playlists:
            print(f"Cannot delete playlist {playlist_name}: Playlist does not exist")
            return
        print(f"Deleted playlist: {playlist_name}")
        del self.playlists[playlist_name.lower()]

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        all_videos = self.video_library.get_all_videos()
        sorted_videos = sorted(all_videos, key=lambda x: x.title)
        count = 0
        search_videos = []

        for i in all_videos:
            if search_term.lower() in i.title.lower():
                if count == 0:
                    print(f"Here are the results for {search_term}:")
                    count = count + 1
                if i.video_id not in self.flagged_videos:
                    search_videos.append(i.video_id)
                    title_txt = str(i.title)
                    video_id_txt = "(" + str(i.video_id) + ")"
                    tag_txt = "[" + " ".join(i.tags) + "]"
                    print(f"{count}) {title_txt} {video_id_txt} {tag_txt}")

        if count >= 1:
            print((
                    "Would you like to play any of the above? If yes, specify the number of the video. \n"
                    "If your answer is not a valid number, we will assume it's a no."))
            try:
                play_above = int(input())
            except ValueError:
                return

            if 0 < play_above <= count:
                self.play_video(search_videos[play_above - 1])
            else:
                return

        else:
            print(f"No search results for {search_term}")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        all_videos = self.video_library.get_all_videos()
        sorted_videos = sorted(all_videos, key=lambda x: x.title)
        count = 0
        search_videos = []

        for i in all_videos:
            if video_tag.lower() in i.tags:
                if count == 0:
                    print(f"Here are the results for {video_tag}:")
                    count = count + 1
                if i.video_id not in self.flagged_videos:
                    search_videos.append(i.video_id)
                    title_txt = str(i.title)
                    video_id_txt = "(" + str(i.video_id) + ")"
                    tag_txt = "[" + " ".join(i.tags) + "]"
                    print(f"{count}) {title_txt} {video_id_txt} {tag_txt}")

        if count >= 1:
            print(
                    "Would you like to play any of the above? If yes, specify the number of the video. \n"
                    "If your answer is not a valid number, we will assume it's a no.")
            try:
                play_above = int(input())

            except ValueError:
                return

            if 0 < play_above <= count:
                self.play_video(search_videos[play_above - 1])
            else:
                return

        else:
            print(f"No search results for {video_tag}")


    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """

        if not flag_reason:
            flag_reason = "Not supplied"

        if not self.video_library.videos.get(video_id, None):
            print(f"Cannot flag video: Video does not exist")
            return

        if video_id in self.flagged_videos:
            print("Cannot flag video: Video is already flagged")
            return

        if self.status_codes['is_playing'] and self.status_codes['current_video_id'].video_id == video_id:
            self.stop_video()

        self.flagged_videos[video_id] = Flagged(video_id)
        self.flagged_videos[video_id].reason = flag_reason
        self.flagged_videos[video_id].status = True


        print(f"Successfully flagged video: {self.video_library.get_video(video_id).title} (reason: {flag_reason})")



    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        if not self.video_library.videos.get(video_id, None):
            print(f"Cannot remove flag from video: Video does not exist")
            return

        if video_id in self.flagged_videos:
            del self.flagged_videos[video_id]
            print(f"Successfully removed flag from video: {self.video_library.get_video(video_id).title}")
        else:
            print("Cannot remove flag from video: Video is not flagged")

