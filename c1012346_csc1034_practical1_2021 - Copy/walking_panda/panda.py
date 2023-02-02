from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from panda3d.core import Fog
from panda3d.core import NodePath


class WalkingPanda(ShowBase):
    def __init__(self, no_rotate=True, scale=1, my_sound=True, color=True, my_fog=True, scenery=True):
        ShowBase.__init__(self)

        # The Worked Practical.
        # Load the environment model.
        self.scene = self.loader.loadModel("models/environment")

        # Re-parent the model to render.
        self.scene.reparentTo(self.render)
        # Apply scale and position transforms on the model.
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)

        # Add the spinCameraTask procedure to the task manager.
        if not no_rotate:
            self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")
        else:
            self.taskMgr.add(self.stopCameraTask, "StopCameraTask")

        # Load and transform the panda actor.
        self.pandaActor = Actor("models/panda-model",
                                {"walk": "models/panda-walk4"})

        # Extended practical argument parsing: Changing scale of panda.
        if scale != None:
            self.pandaActor.setScale((0.005 * float(scale)), (0.005 * float(scale)), (0.005 * float(scale)))

        # Extended practical argument parsing: Adding fog in my scenery
        if my_fog:
            myFog = Fog("distantFog")
            myFog.setColor(0.2, 0, 0)
            myFog.setExpDensity(0.01)
            render.setFog(myFog)

        # Extended practical argument parsing: Changing colour of the scenery
        if scenery:
            self.scene.setColor(0.5, 0.1, 1)

        # Extended practical argument parsing: Changing colour of the panda.
        if color:
            self.pandaActor.setColor(0.18, 0.28, 0.38, 0.48)

        # Extended practical: A multimedia experience.
        if my_sound:
            my_sound = self.loader.loadSfx("walking_panda/sample3.wav")
            my_sound.play()

        self.pandaActor.reparentTo(self.render)

        # Loop its animation.
        self.pandaActor.loop("walk")

    # Define a procedure to move the camera.
    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20.0 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont

    def stopCameraTask(self, task):
        angleDegrees = task.time * 0.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20.0 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont
