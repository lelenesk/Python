
import ffmpeg 
import pytube
import time

import pytube

link = 'https://youtu.be/1MobY_vR7-g'
yt = pytube.YouTube(link, use_oauth=True, allow_oauth_cache=True)

print('Title:', yt.title)
print('Author:', yt.author)
print('Number of views:', yt.views)
print('Length of video:', yt.length, 'seconds')
yt.streams.get_highest_resolution().download()
print('Video successfullly downloaded from', link)


def clean_filename(name):
    forbidden_chars = '"*\\/\'.|?:<>'
    filename = (''.join([x if x not in forbidden_chars else '#' for x in name])).replace('  ', ' ').strip()
    if len(filename) >= 176:
        filename = filename[:170] + '...'
    return filename


def download_video(link, res_level='FHD'):
    ti = time.time()
    yt = pytube.YouTube(link, use_oauth=True, allow_oauth_cache=True)
    print(yt.title, '|', yt.author, '|', yt.publish_date.strftime("%Y-%m-%d"), '|', yt.views, '|', yt.length, 'sec')

    if res_level == '4K':
        dynamic_streams = ['2160p|160kbps', '1440p|160kbps', '1080p|160kbps', '720p|160kbps', '720p|128kbps',
                           '480p|160kbps', '480p|128kbps']
    elif res_level == 'FHD':
        dynamic_streams = ['1080p|160kbps', '720p|160kbps', '720p|128kbps', '480p|160kbps', '480p|128kbps']
    for ds in dynamic_streams:
        try:
            yt.streams.filter(res=ds.split('|')[0], progressive=False).first().download(filename='video.mp4')
            yt.streams.filter(abr=ds.split('|')[1], progressive=False).first().download(filename='audio.mp3')
            break
        except:
            continue

    audio = ffmpeg.input('audio.mp3')
    video = ffmpeg.input('video.mp4')
    filename = 'C:\\Users\\GEPHAZ1\\YT_dwnld\\' + clean_filename(yt.title)

    duplicated = ['', '1', '2', '3', '4', '5']
    for dup in duplicated:
        try:
            ffmpeg.output(audio, video, filename + dup + '.mp4').run()
            break
        except:
            continue

    print(ds, 'video successfully downloaded from', link)
    print('Time taken: {:.0f} sec'.format(time.time() - ti))
