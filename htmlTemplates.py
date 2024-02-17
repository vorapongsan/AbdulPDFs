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
        <img src="https://scontent.fbkk28-1.fna.fbcdn.net/v/t39.30808-6/367007988_754186749840469_6593569203165393446_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=efb6e6&_nc_eui2=AeGnME12TDTeufEeKTuX-vyMg_hkK7bacwiD-GQrttpzCDStQnO4cskb4xdDKLKF4eRwhlo6SJseB_OdD72bNBTE&_nc_ohc=WvmJCYiMw5gAX-MMBAN&_nc_ht=scontent.fbkk28-1.fna&oh=00_AfCfTT-6B9IHQ1No3hqlmzDISVXgmjMiCLe2P59P035O5Q&oe=65D5460A">
     </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
           <img src="https://scontent.fbkk28-1.fna.fbcdn.net/v/t39.30808-6/352133705_797892815194999_4951464042365799110_n.jpg?_nc_cat=104&ccb=1-7&_nc_sid=efb6e6&_nc_eui2=AeG3X_Z1Ee85rSgyq1Gcxz5RSxhgGntceRVLGGAae1x5FaDH3DuLujY4bauXRXl2q2UZmPO6pjc0-AYjbp0x76WC&_nc_ohc=Du6mLnXHJ7QAX9u0-AM&_nc_ht=scontent.fbkk28-1.fna&oh=00_AfC33-Q5jOYm9y_pTyaiJ1UQYGGKYD-fCxjKS2SRDboVYA&oe=65D447E7" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''