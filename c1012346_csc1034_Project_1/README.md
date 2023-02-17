CSC1034: Practical 1
====================
Portfolio 1
===========
---
### <u> My remote run commands: </u>

| Terminal commands                                                                  | Description                                                                                                                                                                                                                                                                                                                     |
|------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `python walk_panda.py`                                                             | Run this command to show panda without any additional features in other words, *the worked practical*.                                                                                                                                                                                                                          |
| `python walk_panda.py --no-rotate` <br/>OR <br/>`python walk_panda.py -r`          | Run this command to stop the camera from rotating. This is the last part of the *worked practical* where I used an if statement. I have also added the shortcut you can use to run *--no-rotate* which is *-r*.                                                                                                                 |
| `python walk_panda.py --scale 2` <br/>OR <br/>`python walk_panda.py -s 2`          | Run this command to show panda increase or decrease in size. Change the 2 to any number to change the size. I have also added the shortcut you can use to run *--scale 2* which is *-s 2*. For scale you have to input a value when running the command on terminal otherwise an error comes up saying it expected an argument. |
| `python walk_panda.py --color`<br/> OR <br/>`python walk_panda.py -c`              | Run this command to change the colour of the panda as a part of the *extended practical*. I have also added the shortcut you can use to run *--color* which is *-c*.                                                                                                                                                            |
| `python walk_panda.py --my_fog`<br/> OR <br/>`python walk_panda.py -f`             | Run this command to fog in the background of panda as a part of the *extended practical*. I have also added the shortcut you can use to run *--my_fog* which is *-f*.                                                                                                                                                           |
| `python walk_panda.py --scenery`<br/> OR <br/>`python walk_panda.py -sc`           | Run this command to change the colour of the scenery as a part of the *extended practical*. I have also added the shortcut you can use to run *--scenery* which is *-sc*.                                                                                                                                                       |
| `python walk_panda.py --my_sound`<br/> OR <br/>`python walk_panda.py -sd`          | Run this command to add music to the panda as the second part of the *extended practical: multi-media*. I have also added the shortcut you can use to run *--my_sound* which is *-sd*.                                                                                                                                          |
| `python walk_panda.py --scale 2 --color --my_fog --scenery --my_sound --no-rotate` | Run this command to have all arguments taking effect on the panda.                                                                                                                                                                                                                                                              |
| `python walk_panda.py -s 2 -c -f -sc -sd -r`                                       | Run this command to have all arguments taking effect on the panda but by using shortcuts.                                                                                                                                                                                                                                       |
| `python walk_panda.py -h`                                                          | Run this code to find from the terminal what each argument parser does.                                                                                                                                                                                                                                                         |

### <u> Requirements: </u>
1. Panda3D
2. Python 3.10
3. Complete setup of Virtual environment
4. pip