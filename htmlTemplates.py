css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://scontent.fbkk28-1.fna.fbcdn.net/v/t39.30808-6/428659454_855853106340499_1221528150201157783_n.jpg?stp=cp6_dst-jpg&_nc_cat=102&ccb=1-7&_nc_sid=3635dc&_nc_eui2=AeHOBrj6IdwCXR_hHHJdkd0i1Xyiu7yNJqLVfKK7vI0momIiEgXyZPPCXU0cQ8r8Bhrj8gY9oXsg4oUM-Vn6j8V0&_nc_ohc=UQgLhzE5Gu4AX91DBfR&_nc_ht=scontent.fbkk28-1.fna&oh=00_AfB2qBupfHTqluF1yAC8jpNDcIIVtcy-WZMT2_pFBERvjw&oe=65D4BBD1">
     </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://scontent.fbkk28-1.fna.fbcdn.net/v/t39.30808-6/367007988_754186749840469_6593569203165393446_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=efb6e6&_nc_eui2=AeGnME12TDTeufEeKTuX-vyMg_hkK7bacwiD-GQrttpzCDStQnO4cskb4xdDKLKF4eRwhlo6SJseB_OdD72bNBTE&_nc_ohc=WvmJCYiMw5gAX-MMBAN&_nc_ht=scontent.fbkk28-1.fna&oh=00_AfCfTT-6B9IHQ1No3hqlmzDISVXgmjMiCLe2P59P035O5Q&oe=65D5460A">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''