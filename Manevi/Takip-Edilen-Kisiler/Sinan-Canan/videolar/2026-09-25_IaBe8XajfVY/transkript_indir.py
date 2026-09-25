"""YouTube videosunun Türkçe transkriptini zaman damgalı Markdown olarak indirir.

Kullanım: python3 transkript_indir.py <video_id> [cikti.md]
"""
import sys

from youtube_transcript_api import YouTubeTranscriptApi


def main():
    video_id = sys.argv[1] if len(sys.argv) > 1 else "IaBe8XajfVY"
    out = sys.argv[2] if len(sys.argv) > 2 else "transkript.md"
    parts = YouTubeTranscriptApi().fetch(video_id, languages=["tr", "en"])
    with open(out, "w", encoding="utf-8") as f:
        f.write(f"# Transkript — https://youtu.be/{video_id}\n\n")
        for p in parts:
            m, s = divmod(int(p.start), 60)
            f.write(f"**[{m:02d}:{s:02d}]** {p.text}  \n")
    print(f"Yazıldı: {out}")


if __name__ == "__main__":
    main()
