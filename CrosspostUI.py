import sys
import tweepy
import atproto
from atproto import Client
from atproto.exceptions import (
    LoginRequiredError,
    BadRequestError,
    ModelError,
    NetworkError,
    InvalidAtUriError,
)
from PyQt5.QtWidgets import QApplication, QDialogButtonBox, QMainWindow, QMenu, QMenuBar, QFileDialog, QTextEdit, QPushButton, QVBoxLayout, QLabel,QFormLayout, QRadioButton, QButtonGroup, QWidget, QDialog, QLineEdit
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class PostApp(QMainWindow):
    def __init__(self):
        super().__init__()

        
        self.API_KEY = ""
        self.API_SECRET = ""
        self.ACCESS_TOKEN = ""
        self.ACCESS_TOKEN_SECRET = ""
        self.bsky_login = "" 
        self.bsky_pw = "#"  

        self.post_twitter = True
        self.post_bsky = True

        self.initUI()


    def initUI(self):
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Post App')

        self.create_menu()

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()

        self.text_area = QTextEdit()
        layout.addWidget(self.text_area)

        self.media_label = QLabel()
        layout.addWidget(self.media_label)

        self.media_path = None
        self.media_button = QPushButton('Attach Media')
        self.media_button.clicked.connect(self.attach_media)
        layout.addWidget(self.media_button)

        self.post_button = QPushButton('Post')
        self.post_button.clicked.connect(self.post)
        layout.addWidget(self.post_button)

        self.central_widget.setLayout(layout)

    def create_menu(self):
        menubar = QMenuBar(self)
        self.setMenuBar(menubar)

        file_menu = menubar.addMenu('File')
        file_menu.addAction('Exit', self.close)

        settings_menu = menubar.addMenu('Settings')
        
        self.dlgX = ConfigureXTwitterDialog(self)
        self.dlgBsky = ConfigureBlueSkyDialog(self)
        self.dlgMastodon = ConfigureMastodonDialog(self)
        self.dlgThreads = ConfigureThreadsDialog(self)


        settings_menu.addAction('Configure X/Twitter Login', self.openDlgX)
        settings_menu.addAction('Configure Bluesky Login', self.openDlgBsky)
        settings_menu.addAction('Configure Mastodon', self.openDlgMastodon)
        settings_menu.addAction('Configure Threads Login', self.openDlgThreads)



        platform_menu = menubar.addMenu('Platform')   # Replaced with checkbox actions for toggling platforms
        self.post_twitter_action = platform_menu.addAction('Post to Twitter')
        self.post_twitter_action.setCheckable(True)
        self.post_twitter_action.setChecked(True)
        self.post_twitter_action.triggered.connect(self.toggle_twitter)

        self.post_bsky_action = platform_menu.addAction('Post to Bluesky')
        self.post_bsky_action.setCheckable(True)
        self.post_bsky_action.setChecked(True)
        self.post_bsky_action.triggered.connect(self.toggle_bsky)

    def openDlgX(self):
        self.dlgX.show()
    
    def openDlgBsky(self):
        self.dlgBsky.show()

    def openDlgMastodon(self):
        self.dlgMastodon.show()

    def openDlgThreads(self):
        self.dlgThreads.show()
    
    def attach_media(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Media File", "", "Image Files (*.jpg *.png *.jpeg);;Video Files (*.mp4 *.avi *.mov)")
        if file_path:
            self.media_path = file_path
            if file_path.endswith(('.jpg', '.png', '.jpeg')):
                pixmap = QPixmap(file_path)
                pixmap = pixmap.scaled(400, 400, Qt.KeepAspectRatio)  # Resize image
                self.media_label.setPixmap(pixmap)
            elif file_path.endswith(('.mp4', '.avi', '.mov')):
                self.media_label.setText(file_path)

    def post(self):
        tweet = self.text_area.toPlainText()
        if len(tweet) > 280:
            print("Length exceeds the maximum character length")
            return

        if self.post_twitter:
            try:
                api = tweepy.Client(
                    consumer_key=self.API_KEY,
                    consumer_secret=self.API_SECRET,
                    access_token=self.ACCESS_TOKEN,
                    access_token_secret=self.ACCESS_TOKEN_SECRET
                )

                if self.media_path and self.media_path.endswith(('.jpg', '.png', '.jpeg')):
                    media = api.upload_media(media=self.media_path)
                    response = api.create_tweet(text=tweet, media_ids=[media.media_id])
                elif self.media_path and self.media_path.endswith(('.mp4', '.avi', '.mov')):
                    print("Video upload is not supported")
                    return
                else:
                    response = api.create_tweet(text=tweet)
            except tweepy.TweepyException as e:
                print(f"Error: Check Settings and rerun script! {e}")

        if self.post_bsky:
            bsky_client = Client()
            try:
                bsky_client.login(self.bsky_login, self.bsky_pw)
                post = bsky_client.send_post(tweet)
                print("Successful Bluesky post")
            except LoginRequiredError as e:
                print(f"Login failed: {e}")

    def toggle_twitter(self):
        self.post_twitter = self.post_twitter_action.isChecked()

    def toggle_bsky(self):
        self.post_bsky = self.post_bsky_action.isChecked()

class ConfigureXTwitterDialog(QDialog):
    def __init__(self, parent=None):
        super(ConfigureXTwitterDialog, self).__init__(parent)
        self.setWindowTitle("Configure X/Twitter Login")
        layout = QFormLayout()
        self.setLayout(layout)
        
        # Example Input Field
        self.twitterHandleInput = QLineEdit()
        layout.addRow(QLabel("Twitter Handle:"), self.twitterHandleInput)
        
        # Dialog Buttons
        buttons = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        buttonBox = QDialogButtonBox(buttons)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)
        layout.addRow(buttonBox)

        def getInputs(self):
            return self.twitterHandleInput.text()

class ConfigureBlueSkyDialog(QDialog):
    def __init__(self, parent=None):
        super(ConfigureBlueSkyDialog, self).__init__(parent)
        self.setWindowTitle("Configure X/Twitter Login")
        layout = QFormLayout()
        self.setLayout(layout)
        
        # Example Input Field
        self.twitterHandleInput = QLineEdit()
        layout.addRow(QLabel("Twitter Handle:"), self.twitterHandleInput)
        
        # Dialog Buttons
        buttons = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        buttonBox = QDialogButtonBox(buttons)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)
        layout.addRow(buttonBox)

        # Optionally, add a method to retrieve input values when accepted
        def getInputs(self):
            return self.twitterHandleInput.text()
        
class ConfigureMastodonDialog(QDialog):
    def __init__(self, parent=None):
        super(ConfigureMastodonDialog, self).__init__(parent)
        self.setWindowTitle("Configure X/Twitter Login")
        layout = QFormLayout()
        self.setLayout(layout)
        
        # Example Input Field
        self.twitterHandleInput = QLineEdit()
        layout.addRow(QLabel("Twitter Handle:"), self.twitterHandleInput)
        
        # Dialog Buttons
        buttons = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        buttonBox = QDialogButtonBox(buttons)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)
        layout.addRow(buttonBox)

class ConfigureThreadsDialog(QDialog):
    def __init__(self, parent=None):
        super(ConfigureThreadsDialog, self).__init__(parent)
        self.setWindowTitle("Configure X/Twitter Login")
        layout = QFormLayout()
        self.setLayout(layout)
        
        # Example Input Field
        self.twitterHandleInput = QLineEdit()
        layout.addRow(QLabel("Twitter Handle:"), self.twitterHandleInput)
        
        # Dialog Buttons
        buttons = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        buttonBox = QDialogButtonBox(buttons)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)
        layout.addRow(buttonBox)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PostApp()
    window.show()
    sys.exit(app.exec_())