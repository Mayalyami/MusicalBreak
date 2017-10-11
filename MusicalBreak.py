import time
import webbrowser
import random

breaks = 16
count = 0
song = ['https://www.youtube.com/watch?v=XsTjI75uEUQ','https://www.youtube.com/watch?v=so6ExplQlaY',
'https://www.youtube.com/watch?v=TG5hps0ZLgE','https://www.youtube.com/watch?v=MGTIx68sjGc',
'https://www.youtube.com/watch?v=kcihcYEOeic','https://www.youtube.com/watch?v=stNT4X2BZtE',
'https://www.youtube.com/watch?v=dXcBA4mFYQk','https://www.youtube.com/watch?v=LvOoQ0Ff2nA',
'https://www.youtube.com/watch?v=oDiRuvJLHYs','https://www.youtube.com/watch?v=w_WoJNWjUBk',
'https://www.youtube.com/watch?v=IGBwmorKeug','https://www.youtube.com/watch?v=jSzu7Aq5zIQ',
'https://www.youtube.com/watch?v=kcR1dK4l4bo','https://www.youtube.com/watch?v=J8bepTpicuM',
'https://www.youtube.com/watch?v=J712_dwLL2g','https://www.youtube.com/watch?v=ALyRSmcEHtw',
'https://www.youtube.com/watch?v=swAicg0GjNg','https://www.youtube.com/watch?v=dXTLomOF_R4',
'https://www.youtube.com/watch?v=shCWqFopC-U','https://www.youtube.com/watch?v=QgaTQ5-XfMM',
'https://www.youtube.com/watch?v=mJ_fkw5j-t0','https://www.youtube.com/watch?v=u2Yk1CEgc4g',
'https://www.youtube.com/watch?v=WZjFMj7OHTw','https://www.youtube.com/watch?v=iO7ySn-Swwc']

while (count < breaks):
  print("This break program started on "+ time.ctime())
  time.sleep(10800)
  webbrowser.open(random.choice(song))
  time.sleep(300)
  count = count + 1
