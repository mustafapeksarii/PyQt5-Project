from PyQt5.QtCore import QDir, Qt, QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (QMainWindow, QWidget, QPushButton, QApplication,
                             QLabel, QFileDialog, QStyle, QVBoxLayout, QAction,QHBoxLayout, QSlider, QSizePolicy)
from PyQt5.QtGui import QIcon, QPalette
import sys

class VideoPlayer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 Video Player")

        p = self.palette()
        p.setColor(QPalette.Window, Qt.darkGray)
        self.setPalette(p)
        # *********************************************************************************
        openAction = QAction(QIcon('open.png'), '&Open', self)
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Open movie')
        openAction.triggered.connect(self.openFile)
        # *********************************************************************************
        exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.exitCall)
        # *********************************************************************************
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&File')
        fileMenu.addAction(openAction)
        fileMenu.addAction(exitAction)
        # *********************************************************************************
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu("&Edit")
        fileMenu.addAction(openAction)
        # *********************************************************************************
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu("&Window")
        fileMenu.addAction(openAction)
        # *********************************************************************************
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu("&Help")
        fileMenu.addAction(openAction)
        # *********************************************************************************
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        videoWidget = QVideoWidget()

        self.positionSlider = QSlider(Qt.Horizontal)
        self.positionSlider.setRange(0, 0)
        self.positionSlider.sliderMoved.connect(self.setPosition)
        self.errorLabel = QLabel()
        self.errorLabel.setSizePolicy(QSizePolicy.Preferred,QSizePolicy.Maximum)
        wid = QWidget(self)
        self.setCentralWidget(wid)
        controlLayout = QHBoxLayout()
        controlLayout.setContentsMargins(0, 0, 0, 0)
        controlLayout.addWidget(self.positionSlider)
        # *********************************************************************************
        self.playButton = QPushButton()
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playButton.setStyleSheet("border : 2px solid black;"
                                      "background : white;"
                                      "border-style: inset;"
                                      "border-radius 4px;")
        self.playButton.clicked.connect(self.play)
        #*********************************************************************************
        self.pauseButton = QPushButton()
        self.pauseButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
        self.pauseButton.setStyleSheet("border : 2px solid black;"
                                       "background : white;"
                                       "border-style: inset;"
                                       "border-radius 4px;")
        self.pauseButton.clicked.connect(self.pause)
        # *********************************************************************************
        self.stopButton = QPushButton()
        self.stopButton.setIcon(self.style().standardIcon(QStyle.SP_MediaStop))
        self.stopButton.setStyleSheet("border : 2px solid black;"
                                      "background : white;"
                                      "border-style : inset;"
                                      "border-radius 4px;")
        # "QPushbutton : hover {background-color: red;}")
        self.stopButton.clicked.connect(self.stop)
        # *********************************************************************************
        self.volumeButton = QPushButton()
        self.volumeButton.setIcon(self.style().standardIcon(QStyle.SP_MediaVolume))
        self.volumeButton.setStyleSheet("border : 2px solid black;"
                                        "background : white;"
                                        "border-style: inset;"
                                        "border-radius 4px;")
        self.volumeButton.clicked.connect(self.volume)
        # *********************************************************************************
        self.muteButton = QPushButton()
        self.muteButton.setIcon(self.style().standardIcon(QStyle.SP_MediaVolumeMuted))
        self.muteButton.setStyleSheet("border : 2px solid black;"
                                        "background : white;"
                                        "border-style: inset;"
                                        "border-radius 4px;")
        self.muteButton.clicked.connect(self.mute)
        # *********************************************************************************
        self.deleteButton = QPushButton()
        self.deleteButton.setIcon(self.style().standardIcon(QStyle.SP_DialogCancelButton))
        self.deleteButton.setStyleSheet("border : 2px solid black;"
                                      "background : white;"
                                      "border-style: inset;"
                                      "border-radius 4px;")
        self.deleteButton.clicked.connect(self.delete)
        # *********************************************************************************
        self.nextButton = QPushButton()
        self.nextButton.setIcon(self.style().standardIcon(QStyle.SP_MediaSkipForward))
        self.nextButton.setStyleSheet("border : 2px solid black;"
                                      "background : white;"
                                      "border-style: inset;"
                                      "border-radius 4px;")
        self.nextButton.clicked.connect(self.next)
        # *********************************************************************************
        self.backButton = QPushButton()
        self.backButton.setIcon(self.style().standardIcon(QStyle.SP_MediaSkipBackward))
        self.backButton.setStyleSheet("border : 2px solid black;"
                                      "background : white;"
                                      "border-style: inset;"
                                      "border-radius 4px;")
        self.backButton.clicked.connect(self.back)
        # *********************************************************************************
        self.openButton = QPushButton()
        self.openButton.setIcon(self.style().standardIcon(QStyle.SP_DialogOpenButton))
        self.openButton.setStyleSheet("border : 2px solid black;"
                                      "background : white;"
                                      "border-style: inset;"
                                      "border-radius 4px;")
        self.openButton.clicked.connect(self.openFile)
        # *********************************************************************************
        self.button1 = QPushButton()
        self.button1.setFixedSize(80,30)
        self.button1.setIcon(self.style().standardIcon(QStyle.SP_MessageBoxQuestion))
        self.button1.setStyleSheet("border : 2px solid black;"
                                      "background : white;"
                                      "border-style: inset;"
                                      "border-radius 4px;")
        #self.button1.clicked.connect(self.openFile)
        self.button2 = QPushButton()
        self.button2.setFixedSize(80, 30)
        self.button2.setIcon(self.style().standardIcon(QStyle.SP_DialogDiscardButton))
        self.button2.setStyleSheet("border : 2px solid black;"
                                   "background : white;"
                                   "border-style: inset;"
                                   "border-radius 4px;")
        # *********************************************************************************
        self.button3 = QPushButton()
        self.button3.setFixedSize(80, 30)
        self.button3.setIcon(self.style().standardIcon(QStyle.SP_FileDialogListView))
        self.button3.setStyleSheet("border : 2px solid black;"
                                   "background : white;"
                                   "border-style: inset;"
                                   "border-radius 4px;")
        # *********************************************************************************
        self.button4 = QPushButton()
        self.button4.setFixedSize(80, 520)
        # self.button3.setIcon(self.style().standardIcon(QStyle.SP_DialogOpenButton))
        self.button4.setStyleSheet("border : 2px solid black;"
                                   "background : white;"
                                   "border-style: inset;"
                                   "border-radius 4px;")
        # *********************************************************************************
        widget = QWidget(self)
        self.setCentralWidget(widget)

        layout = QHBoxLayout()
        layout1 = QVBoxLayout()
        layout2 = QHBoxLayout()
        layout3 = QHBoxLayout()
        layout4 = QVBoxLayout()
        layout5 = QVBoxLayout()
        layout6 = QVBoxLayout()
        layout7 = QVBoxLayout()
        layout8 = QVBoxLayout()
        layout9 = QHBoxLayout()
        layout10 = QHBoxLayout()
        layout.addLayout(layout5)
        layout.addLayout(layout4)
        layout4.addLayout(layout1)
        layout4.addLayout(layout8)
        layout4.addLayout(layout2)
        layout4.addLayout(layout3)
        layout5.addLayout(layout7)
        layout5.addLayout(layout6)
        layout2.addLayout(layout10)
        layout2.addLayout(layout9)

        layout7.addWidget(self.button1)
        layout7.addWidget(self.button2)
        layout7.addWidget(self.button3)
        layout6.addWidget(self.button4)
        layout1.addWidget(videoWidget)
        layout10.addWidget(self.openButton)
        layout10.addWidget(self.deleteButton)
        layout9.addWidget(self.pauseButton)
        layout9.addWidget(self.muteButton)
        layout10.addWidget(self.stopButton)
        layout3.addWidget(self.backButton)
        layout3.addWidget(self.playButton)
        layout3.addWidget(self.nextButton)
        layout9.addWidget(self.volumeButton)

        layout8.addWidget(self.errorLabel)
        layout8.addLayout(controlLayout)

        widget.setLayout(layout)
        wid.setLayout(layout8)
        self.mediaPlayer.setVideoOutput(videoWidget)
        self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
        self.mediaPlayer.positionChanged.connect(self.positionChanged)
        self.mediaPlayer.durationChanged.connect(self.durationChanged)
        self.mediaPlayer.error.connect(self.handleError)
    # *********************************************************************************
    def mediaStateChanged(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
           self.playButton.setIcon(
           self.style().standardIcon(QStyle.SP_MediaPause))
        else:
           self.playButton.setIcon(
           self.style().standardIcon(QStyle.SP_MediaPlay))
    def positionChanged(self, position):
        self.positionSlider.setValue(position)
    def durationChanged(self, duration):
        self.positionSlider.setRange(0, duration)
    def setPosition(self, position):
        self.mediaPlayer.setPosition(position)
    def handleError(self):
        self.playButton.setEnabled(False)
        self.errorLabel.setText("Error: " + self.mediaPlayer.errorString())
    def openFile(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Movie",QDir.homePath())
        if fileName != '':
            self.mediaPlayer.setMedia(
                QMediaContent(QUrl.fromLocalFile(fileName)))
    def play(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()
    def stop(self):
        if self.mediaPlayer.state() ==QMediaPlayer.StoppedState:
            self.mediaPlayer.play()
        else:
            self.mediaPlayer.stop()
    def volume(self):
        if self.mediaPlayer.state() ==QMediaPlayer.volumeState:
            self.mediaPlayer.volume()
        else:
            self.mediaPlayer.volume()
    def mute(self):
        if self.mediaPlayer.state() ==QMediaPlayer.muteState:
            self.mediaPlayer.mute()
        else:
            self.mediaPlayer.mute()
    def delete(self):
        if self.mediaPlayer.state() ==QMediaPlayer.deleteState:
            self.mediaPlayer.delete()
        else:
            self.mediaPlayer.delete()
    def pause(self):
        if self.mediaPlayer.state() ==QMediaPlayer.pausedstate:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.pause()
    def next(self):
        if self.mediaPlayer.state() ==QMediaPlayer.nextState:
            self.mediaPlayer.next()
        else:
            self.mediaPlayer.next()
    def back(self):
        if self.mediaPlayer.state() ==QMediaPlayer.backState:
            self.mediaPlayer.back()
        else:
            self.mediaPlayer.back()
    def exitCall(self):
        sys.exit(app.exec_())
    # *********************************************************************************

app = QApplication(sys.argv)
videoplayer = VideoPlayer()
videoplayer.resize(800, 600)
videoplayer.show()
sys.exit(app.exec_())
