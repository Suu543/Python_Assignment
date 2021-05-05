from tkinter import *
import time


class StopWatch(Frame):
    """ Implements a stop watch frame widget. """

    def __init__(self, parent=None, **kw):
        Frame.__init__(self, parent, kw)
        self._start = 0.0
        self._elapsedtime = 0.0
        self._running = 0
        self.timestr = StringVar()
        self.makeWidgets()

    def makeWidgets(self):
        """ Make the time label. """
        l = Label(self, height=5, text="40", font=(
            "Arial 40 bold"), textvariable=self.timestr)
        self._setTime(self._elapsedtime)
        l.pack(fill=X, expand=NO, pady=2, padx=2)

    def _update(self):
        """ Update the label with elapsed time. """
        self._elapsedtime = time.time() - self._start
        self._setTime(self._elapsedtime)
        self._timer = self.after(50, self._update)

    def _setTime(self, elap):
        """ Set the time string to Minutes:Seconds:Hundreths """
        minutes = int(elap/60)
        seconds = int((elap - minutes * 60.0))
        hseconds = int((elap - minutes * 60.0 - seconds) * 100)
        self.timestr.set('%01d:%03d' % (seconds, hseconds))

    def Start(self):
        """ Start the stopwatch, ignore if running. """
        if not self._running:
            self._start = time.time() - self._elapsedtime
            self._update()
            self._running = 1

    def Stop(self):
        """ Stop the stopwatch, ignore if stopped. """
        if self._running:
            self.after_cancel(self._timer)
            self._elapsedtime = time.time() - self._start
            self._setTime(self._elapsedtime)
            self._running = 0

    def Reset(self):
        """ Reset the stopwatch. """
        self._start = time.time()
        self._elapsedtime = 0.0
        self._setTime(self._elapsedtime)


def main():
    root = Tk()
    sw = StopWatch(root)
    sw.pack(side=TOP)

    Button(root, width=10, text='Start', bg="green",
           command=sw.Start).pack(side=LEFT)
    Button(root, width=10, text='Stop', bg="red",
           command=sw.Stop).pack(side=LEFT)
    Button(root, width=10, text='Reset', bg="yellow",
           command=sw.Reset).pack(side=LEFT)

    root.mainloop()


if __name__ == '__main__':
    main()
