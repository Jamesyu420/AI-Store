# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import ctypes
import imutils
import cv2
import matplotlib.pyplot as plt
from matplotlib import _pylab_helpers
import time
import datetime


class Ui_MainLayout(QtCore.QObject):

    def setupUi(self, MainLayout):
        MainLayout.setObjectName("MainLayout")
        MainLayout.resize(872, 554)
        self.cam = False
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(MainLayout)
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.LeftWidget = QtWidgets.QWidget(MainLayout)
        self.LeftWidget.setMinimumSize(QtCore.QSize(154, 0))
        self.LeftWidget.setStyleSheet("QWidget#LeftWidget{\n"
                                      "    background:gray;\n"
                                      "    border-top:1px solid white;\n"
                                      "    border-bottom:1px solid white;\n"
                                      "    border-left:1px solid white;\n"
                                      "    border-top-left-radius:10px;\n"
                                      "    border-bottom-left-radius:10px;\n"
                                      "}")
        self.LeftWidget.setObjectName("LeftWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.LeftWidget)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_2.setSpacing(17)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ExitWidget = QtWidgets.QWidget(self.LeftWidget)
        self.ExitWidget.setObjectName("ExitWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.ExitWidget)
        self.horizontalLayout.setSpacing(14)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Btn_mini = QtWidgets.QPushButton(self.ExitWidget)
        self.Btn_mini.setMinimumSize(QtCore.QSize(15, 15))
        self.Btn_mini.setMaximumSize(QtCore.QSize(15, 15))
        self.Btn_mini.setStyleSheet(
            "QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}")
        self.Btn_mini.setText("")
        self.Btn_mini.setIconSize(QtCore.QSize(15, 15))
        self.Btn_mini.setObjectName("Btn_mini")
        self.Btn_mini.clicked.connect(MainLayout.showMaximized)
        self.horizontalLayout.addWidget(self.Btn_mini)
        self.Btn_visit = QtWidgets.QPushButton(self.ExitWidget)
        self.Btn_visit.setMinimumSize(QtCore.QSize(15, 15))
        self.Btn_visit.setMaximumSize(QtCore.QSize(15, 15))
        self.Btn_visit.setStyleSheet(
            "QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}")
        self.Btn_visit.setText("")
        self.Btn_visit.setObjectName("Btn_visit")
        self.Btn_visit.clicked.connect(MainLayout.showMinimized)
        self.horizontalLayout.addWidget(self.Btn_visit)
        self.Btn_close = QtWidgets.QPushButton(self.ExitWidget)
        self.Btn_close.setMinimumSize(QtCore.QSize(15, 15))
        self.Btn_close.setMaximumSize(QtCore.QSize(15, 15))
        self.Btn_close.setStyleSheet(
            "QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}")
        self.Btn_close.setText("")
        self.Btn_close.setObjectName("Btn_close")
        self.Btn_close.clicked.connect(MainLayout.close)
        self.horizontalLayout.addWidget(self.Btn_close)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 4)
        self.verticalLayout_2.addWidget(self.ExitWidget, 0, QtCore.Qt.AlignTop)
        self.BtnWidget = QtWidgets.QWidget(self.LeftWidget)
        self.BtnWidget.setObjectName("BtnWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.BtnWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(17)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Btn_PeopleCounting = QtWidgets.QPushButton(self.BtnWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_PeopleCounting.sizePolicy().hasHeightForWidth())
        self.Btn_PeopleCounting.setSizePolicy(sizePolicy)
        self.Btn_PeopleCounting.setMinimumSize(QtCore.QSize(150, 50))
        self.Btn_PeopleCounting.setSizeIncrement(QtCore.QSize(300, 51))
        self.Btn_PeopleCounting.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.Btn_PeopleCounting.setStyleSheet("QPushButton{border:none;color:white;}\n"
                                              "QPushButton{\n"
                                              "    font: 24pt \"微软雅黑\";\n"
                                              "        border:none;\n"
                                              "        color:white;\n"
                                              "        font-size:25px;\n"
                                              "        height:40px;\n"
                                              "        padding-left:10px;\n"
                                              "        padding-right:10px;\n"
                                              "        text-align:center;\n"
                                              "    }\n"
                                              "    QPushButton:hover{\n"
                                              "        color:black;\n"
                                              "        border:1px solid #F3F3F5;\n"
                                              "        border-radius:10px;\n"
                                              "        background:LightGray;\n"
                                              "    }\n"
                                              "\n"
                                              "")
        self.Btn_PeopleCounting.setObjectName("Btn_PeopleCounting")
        self.Btn_PeopleCounting.clicked.connect(self.counting_loadfile_ui)
        self.verticalLayout.addWidget(self.Btn_PeopleCounting, 0, QtCore.Qt.AlignHCenter)
        self.Btn_FrequenCustomer = QtWidgets.QPushButton(self.BtnWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_FrequenCustomer.sizePolicy().hasHeightForWidth())
        self.Btn_FrequenCustomer.setSizePolicy(sizePolicy)
        self.Btn_FrequenCustomer.setMinimumSize(QtCore.QSize(150, 50))
        self.Btn_FrequenCustomer.setMaximumSize(QtCore.QSize(150, 50))
        self.Btn_FrequenCustomer.setStyleSheet("QPushButton{border:none;color:white;}\n"
                                               "QPushButton{\n"
                                               "    font: 24pt \"微软雅黑\";\n"
                                               "        border:none;\n"
                                               "        color:white;\n"
                                               "        font-size:25px;\n"
                                               "        height:40px;\n"
                                               "        padding-left:10px;\n"
                                               "        padding-right:10px;\n"
                                               "        text-align:center;\n"
                                               "    }\n"
                                               "    QPushButton:hover{\n"
                                               "        color:black;\n"
                                               "        border:1px solid #F3F3F5;\n"
                                               "        border-radius:10px;\n"
                                               "        background:LightGray;\n"
                                               "    }\n"
                                               "\n"
                                               "")
        self.Btn_FrequenCustomer.clicked.connect(self.frequent_video)
        self.Btn_FrequenCustomer.setObjectName("Btn_FrequenCustomer")
        self.verticalLayout.addWidget(self.Btn_FrequenCustomer, 0, QtCore.Qt.AlignHCenter)
        self.Btn_VIP = QtWidgets.QPushButton(self.BtnWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_VIP.sizePolicy().hasHeightForWidth())
        self.Btn_VIP.setSizePolicy(sizePolicy)
        self.Btn_VIP.setMaximumSize(QtCore.QSize(150, 50))
        self.Btn_VIP.setStyleSheet("QPushButton{border:none;color:white;}\n"
                                   "QPushButton{\n"
                                   "    font: 24pt \"微软雅黑\";\n"
                                   "        border:none;\n"
                                   "        color:white;\n"
                                   "        font-size:25px;\n"
                                   "        height:40px;\n"
                                   "        padding-left:10px;\n"
                                   "        padding-right:10px;\n"
                                   "        text-align:center;\n"
                                   "    }\n"
                                   "    QPushButton:hover{\n"
                                   "        color:black;\n"
                                   "        border:1px solid #F3F3F5;\n"
                                   "        border-radius:10px;\n"
                                   "        background:LightGray;\n"
                                   "    }\n"
                                   "\n"
                                   "")
        self.Btn_VIP.setObjectName("Btn_VIP")
        self.verticalLayout.addWidget(self.Btn_VIP, 0, QtCore.Qt.AlignHCenter)
        self.Btn_PrecisionMarketing = QtWidgets.QPushButton(self.BtnWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_PrecisionMarketing.sizePolicy().hasHeightForWidth())
        self.Btn_PrecisionMarketing.setSizePolicy(sizePolicy)
        self.Btn_PrecisionMarketing.setMaximumSize(QtCore.QSize(150, 50))
        self.Btn_PrecisionMarketing.setStyleSheet("QPushButton{border:none;color:white;}\n"
                                                  "QPushButton{\n"
                                                  "    font: 24pt \"微软雅黑\";\n"
                                                  "        border:none;\n"
                                                  "        color:white;\n"
                                                  "        font-size:25px;\n"
                                                  "        height:40px;\n"
                                                  "        padding-left:10px;\n"
                                                  "        padding-right:10px;\n"
                                                  "        text-align:center;\n"
                                                  "    }\n"
                                                  "    QPushButton:hover{\n"
                                                  "        color:black;\n"
                                                  "        border:1px solid #F3F3F5;\n"
                                                  "        border-radius:10px;\n"
                                                  "        background:LightGray;\n"
                                                  "    }\n"
                                                  "\n"
                                                  "")
        self.Btn_PrecisionMarketing.setObjectName("Btn_PrecisionMarketing")
        self.verticalLayout.addWidget(self.Btn_PrecisionMarketing, 0, QtCore.Qt.AlignHCenter)
        self.Btn_Contact = QtWidgets.QPushButton(self.BtnWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_Contact.sizePolicy().hasHeightForWidth())
        self.Btn_Contact.setSizePolicy(sizePolicy)
        self.Btn_Contact.setMaximumSize(QtCore.QSize(150, 50))
        self.Btn_Contact.setStyleSheet("QPushButton{border:none;color:white;}\n"
                                       "QPushButton{\n"
                                       "    font: 24pt \"微软雅黑\";\n"
                                       "        border:none;\n"
                                       "        color:white;\n"
                                       "        font-size:25px;\n"
                                       "        height:40px;\n"
                                       "        padding-left:10px;\n"
                                       "        padding-right:10px;\n"
                                       "        text-align:center;\n"
                                       "    }\n"
                                       "    QPushButton:hover{\n"
                                       "        color:black;\n"
                                       "        border:1px solid #F3F3F5;\n"
                                       "        border-radius:10px;\n"
                                       "        background:LightGray;\n"
                                       "    }\n"
                                       "\n"
                                       "")
        self.Btn_Contact.setObjectName("Btn_PrecisionMarketing_2")
        self.Btn_Contact.clicked.connect(self.open_contact_ui)
        self.verticalLayout.addWidget(self.Btn_Contact, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 1)
        self.verticalLayout_2.addWidget(self.BtnWidget, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.setStretch(1, 10)
        self.horizontalLayout_3.addWidget(self.LeftWidget, 0, QtCore.Qt.AlignHCenter)
        self.RightWidget = QtWidgets.QWidget(MainLayout)
        self.RightWidget.setStyleSheet("QWidget#RightWidget{\n"
                                       "        color:#232C51;\n"
                                       "        background:white;\n"
                                       "        border-top:1px solid darkGray;\n"
                                       "        border-bottom:1px solid darkGray;\n"
                                       "        border-right:1px solid darkGray;\n"
                                       "        border-top-right-radius:10px;\n"
                                       "        border-bottom-right-radius:10px;    \n"
                                       "    }")
        self.RightWidget.setObjectName("RightWidget")
        self.RightLayout = QtWidgets.QVBoxLayout(self.RightWidget)
        self.RightLayout.setContentsMargins(0, -1, -1, -1)
        self.RightLayout.setObjectName("RightLayout")
        self.LblVideo = QtWidgets.QLabel(self.RightWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LblVideo.sizePolicy().hasHeightForWidth())
        self.LblVideo.setSizePolicy(sizePolicy)
        self.LblVideo.setMinimumSize(QtCore.QSize(700, 394))
        self.LblVideo.setMaximumSize(QtCore.QSize(700, 394))
        self.LblVideo.setObjectName("LblVideo")
        self.RightLayout.addWidget(self.LblVideo, 0, QtCore.Qt.AlignHCenter)
        self.Btn_Widget = QtWidgets.QWidget(self.RightWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_Widget.sizePolicy().hasHeightForWidth())
        self.Btn_Widget.setSizePolicy(sizePolicy)
        self.Btn_Widget.setObjectName("Btn_Widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Btn_Widget)
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(7)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Btn_Analysis = QtWidgets.QPushButton(self.Btn_Widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_Analysis.sizePolicy().hasHeightForWidth())
        self.Btn_Analysis.setSizePolicy(sizePolicy)
        self.Btn_Analysis.setMinimumSize(QtCore.QSize(150, 50))
        self.Btn_Analysis.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.Btn_Analysis.setFont(font)
        self.Btn_Analysis.setStyleSheet("QPushButton{\n"
                                        "    background-image:url(./res/common/main_reduction.png);\n"
                                        "    background-repeat:no-repeat;\n"
                                        "    border:none;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "    background-color:#CCCCCC\n"
                                        "}\n"
                                        "QPushButton:pressed{\n"
                                        "    background-color:#888888\n"
                                        "}")
        self.Btn_Analysis.setObjectName("Btn_Analysis")
        self.horizontalLayout_2.addWidget(self.Btn_Analysis)
        self.Btn_Chart = QtWidgets.QPushButton(self.Btn_Widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_Chart.sizePolicy().hasHeightForWidth())
        self.Btn_Chart.setSizePolicy(sizePolicy)
        self.Btn_Chart.setMinimumSize(QtCore.QSize(150, 50))
        self.Btn_Chart.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.Btn_Chart.setFont(font)
        self.Btn_Chart.setStyleSheet("QPushButton{\n"
                                     "    background-image:url(./res/common/main_reduction.png);\n"
                                     "    background-repeat:no-repeat;\n"
                                     "    border:none;\n"
                                     "}\n"
                                     "QPushButton:hover{\n"
                                     "    background-color:#CCCCCC\n"
                                     "}\n"
                                     "QPushButton:pressed{\n"
                                     "    background-color:#888888\n"
                                     "}")
        self.Btn_Chart.setObjectName("Btn_Chart")
        self.horizontalLayout_2.addWidget(self.Btn_Chart)
        self.Btn_Chart.clicked.connect(self.count_chart)
        self.Btn_HomePage = QtWidgets.QPushButton(self.Btn_Widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_HomePage.sizePolicy().hasHeightForWidth())
        self.Btn_HomePage.setSizePolicy(sizePolicy)
        self.Btn_HomePage.setMinimumSize(QtCore.QSize(150, 50))
        self.Btn_HomePage.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.Btn_HomePage.setFont(font)
        self.Btn_HomePage.setStyleSheet("QPushButton{\n"
                                        "    background-image:url(./res/common/main_reduction.png);\n"
                                        "    background-repeat:no-repeat;\n"
                                        "    border:none;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "    background-color:#CCCCCC\n"
                                        "}\n"
                                        "QPushButton:pressed{\n"
                                        "    background-color:#888888\n"
                                        "}")
        self.Btn_HomePage.setObjectName("Btn_HomePage")
        self.horizontalLayout_2.addWidget(self.Btn_HomePage)
        self.RightLayout.addWidget(self.Btn_Widget, 0, QtCore.Qt.AlignHCenter)
        self.RightLayout.setStretch(1, 4)
        self.horizontalLayout_3.addWidget(self.RightWidget)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 8)
        MainLayout.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        MainLayout.setWindowOpacity(0.95)
        MainLayout.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.horizontalLayout_3.setSpacing(0)
        self.retranslateUi(MainLayout)
        QtCore.QMetaObject.connectSlotsByName(MainLayout)

    def retranslateUi(self, MainLayout):
        _translate = QtCore.QCoreApplication.translate
        MainLayout.setWindowTitle(_translate("MainLayout", "商店智能顾客系统"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainLayout.setWindowIcon(icon)
        self.Btn_PeopleCounting.setText(_translate("MainLayout", "客流监测"))
        self.Btn_FrequenCustomer.setText(_translate("MainLayout", "熟客识别"))
        self.Btn_VIP.setText(_translate("MainLayout", "会员信息"))
        self.Btn_PrecisionMarketing.setText(_translate("MainLayout", "精准营销"))
        self.Btn_Contact.setText(_translate("MainLayout", "@联系我们"))
        self.Btn_Analysis.setText(_translate("MainLayout", "分析"))
        self.Btn_Chart.setText(_translate("MainLayout", "图表"))
        self.Btn_HomePage.setText(_translate("MainLayout", "返回主页"))

    def open_contact_ui(self):
        self.contact_ui = ContactUI()
        self.contact_ui.show()

    def counting_loadfile_ui(self):
        self.PeopleCounting_ui = Counting_Loadfile_UI()
        self.PeopleCounting_ui.show()

    def frequent_video(self):
        t = (True, " ")
        ui.video_play(t)

    def video_play(self, video_msg):
        if video_msg[0]:    # True表示调用摄像头
            self.cam = cv2.VideoCapture(0)
        else:
            self.cam = cv2.VideoCapture(video_msg[1])
        self.LblVideo.setAlignment(QtCore.Qt.AlignCenter)
        # 设置定时器 每25毫秒执行实例的play函数以刷新图像
        self._timer = QtCore.QTimer(self)
        self._timer.timeout.connect(self.play)
        self._timer.start(25)

    def play(self):
        """
        从摄像头得到图像 先转换为RGB格式 再生成QImage对象
        再用此QImage刷新LblVideo实例变量 以刷新视频画面
        """
        r, f = self.cam.read()
        if r:
            f = imutils.resize(f, width=700)
            self.LblVideo.setPixmap(QtGui.QPixmap.fromImage(
                QtGui.QImage(cv2.cvtColor(imutils.resize(f, width=700), cv2.COLOR_BGR2RGB),
                             f.shape[1],
                             f.shape[0],
                             QtGui.QImage.Format_RGB888)))

    def count_chart(self):

        fig=plt.figure()
        ax=fig.add_subplot(1,1,1)

        ax.set_xlabel('Time')
        ax.set_ylabel('people_count')
        ax.set_title('')

        line = None
        plt.grid(True)
        plt.ion()
        obsX = []
        obsY = []

        t0 = time.time()
        f=open("people_cout.txt","r")
        s=int(f.readline()[:-1])

        while True:
            t=datetime.datetime.now().second
            obsX.append(datetime.datetime.now().second)
            s=f.readline()[:-1]
            if not s:
                f.close()
                plt.close()
                break
            else:
                s=int(f.readline()[:-1])
            obsY.append(s)

            if line is None:
                line = ax.plot(obsX,obsY,'-g',marker='*')[0]

            line.set_xdata(obsX)
            line.set_ydata(obsY)

            ax.set_xlim([t-10,t+1])
            ax.set_ylim([0,20])
            plt.savefig("1.png")
            x=QtGui.QPixmap("1.png")

            self.LblVideo.setPixmap(x)
            self.mypause(1)

    def mypause(self,interval):
        manager = _pylab_helpers.Gcf.get_active()
        if manager is not None:
            canvas = manager.canvas
            if canvas.figure.stale:
                canvas.draw_idle()
            canvas.start_event_loop(interval)
        else:
            time.sleep(interval)

class ContactUI(QtWidgets.QDialog):
    def __init__(self):
        super(ContactUI, self).__init__()
        self.resize(400, 300)
        self.setWindowTitle("联系我们")
        self.label = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(700, 394))
        self.label.setMaximumSize(QtCore.QSize(700, 394))
        # need to be update
        self.label.setText("商店智能顾客系统\n"
                           "作者：余柏辰 姜琼 李雨芯\n"
                           "商家在经营过程中，为了更好地了解顾客、提高顾客的购物体验，\n进而获得更大的利益，就需要掌握顾客的全方位数据进行分析。"
                           "本作品旨在通过多维度地获取顾客的信息并进行分析，最终\n智能地制定个性化购物推荐方案，主要包括客流监测、常客识别、商品推荐等功能板块。"
                           "通过国产华为云一站式AI开发平台实现开发、并搭配其HiLens硬件\n设备的高时效性软硬件结合的人工智能产品，是本软件的特色。")

    def event(self, event):
        if event.type() == QtCore.QEvent.EnterWhatsThisMode:
            QtWidgets.QWhatsThis.leaveWhatsThisMode()
            self.text_brow.setText('Help')
        return QtWidgets.QDialog.event(self, event)


class Counting_Loadfile_UI(QtWidgets.QDialog):
    def __init__(self):
        super(Counting_Loadfile_UI, self).__init__()
        # self.resize(600,400)
        self.setWindowTitle("选择输入方式")
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        self.Widget = QtWidgets.QWidget()
        self.Widget.setStyleSheet("QWidget:{"
                                  "background: #222222;"
                                  "border-top-left-radius:10px;"
                                  "border-top-right-radius:10px;"
                                  "border-bottom-right-radius:10px"
                                  "border-bottom-left-radius:10px"
                                  "color: #BBBBBB;"
                                  'font-family: "Segoe UI";'
                                  "}")
        self.Widget.setObjectName("Widget")
        layout = QtWidgets.QVBoxLayout(self.Widget)

        # 实例化btn1
        self.btn1 = QtWidgets.QRadioButton("文件导入")
        self.btn1.setChecked(True)
        self.btn1.toggled.connect(lambda: self.btnstate(self.btn1))
        layout.addWidget(self.btn1)

        # 实例化btn2
        self.btn2 = QtWidgets.QRadioButton("实时监测")
        self.btn2.toggled.connect(lambda: self.btnstate(self.btn2))
        layout.addWidget(self.btn2)

        self.btn = QtWidgets.QPushButton("确认")
        self.btn.clicked.connect(lambda: self.btnclick(self.btn))
        layout.addWidget(self.btn)
        self.setLayout(layout)

    def btnstate(self, btn):  # 自定义点击事件函数
        if btn.isChecked():
            return btn.text()
        else:
            return None

    def btnclick(self, btn):
        # flag 用于记录是否调用摄像头，True表示是
        flag = True
        if self.btnstate(self.btn1) != None:
            flag = False
            selectedFile = QtWidgets.QFileDialog.getOpenFileName(self,
                                                                 "Select one file to open",
                                                                 "/home",
                                                                 "Video Files(*.avi *.wmv *.mov *.mpeg *.mpg *.mp4 *.mkv *.rm *.rmvb *.flv)")
        else:
            selectedFile = " "
        self.close()
        ui.video_play((flag, selectedFile[0]))



if __name__ == "__main__":
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    ui = Ui_MainLayout()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())
