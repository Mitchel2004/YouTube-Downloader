# YouTube Downloader

This is a simple program that downloads audio from YouTube videos.
There are a couple of fields for metadata (title, artist, language, etc.) that can be filled in.
The program will create an mp3 file at a chosen location with the filled in title and artist fields as filename.

![YTDL Logo](https://github.com/user-attachments/assets/a3db529a-3fbe-4bf6-84f2-67aaaaeed380)

## How to Use

1. Find a YouTube video that you like and copy the link.
2. Paste the link in the YouTube URL field.
3. Add optional metadata. This is useful for mediaplayers to display the proper information about the audio file.
4. Choose a target directory so the program knows where it needs to create the files.
5. Click the download button.

It's that easy.

## Good to Know
- The program will automatically overwrite existing files with the same name.
- I only tested this on Windows, and also only expect it to work on Windows.
- If you're unsure what some of the metadata means, you can read the ID3 documentation on https://id3.org/id3v2.3.0.
- The program uses [FFmpeg](https://en.wikipedia.org/wiki/FFmpeg) to create the mp3 files. If you wish to use the source code, keep in mind that you need to have it installed.
- Create a new issue on this repository if you need to add other metadata tags or other languages. I didn't include all of them.

## License & Copyright

[Mozilla Public License 2.0](https://www.mozilla.org/MPL/2.0/)

© Mitchel Klijn
