// Server
import java.util.ArrayList;
import java.util.Date;
import java.util.HashMap;

// import Constants.RequestStatus;
// import Constants.UserStatusType;
enum RequestStatus{
    REJECTED, ACCEPTED, PENDING, UNREAD
}
enum UserStatusType{
    ONLINE, OFFLINE
}
// class Constants{
   
//     public static enum RequestStatus{

// }
// }

class AddRequest {
	private User from;
	private User to;
	private Date date;
	RequestStatus status;
	
	public AddRequest(User f, User t, Date d) {
		this.from = f;
		this.to = t;
		this.date = d;
		this.status= RequestStatus.UNREAD;
	}
	
	public RequestStatus getStatus() {
		return status;
	}
	
	public User getFromUser() {
		return from;
	}
	
	public User getToUser() {
		return to;
	}
	
	public Date getDate() {
		return date;
	}

}

class Server {
	private static Server server;
	// db stuff
	HashMap<User, ArrayList<User>> userFriends;
	private HashMap<Integer, User> usersById = new HashMap<Integer, User>();
	private HashMap<String, User> usersByAccountName = new HashMap<String, User>();
	private HashMap<Integer, User> onlineUsers = new HashMap<Integer, User>();
	
	private Server() {
	}
	
	public static Server getInstance() {
		if(server == null) {
			server = new Server();
		}
		return server;
	}
	
	public boolean managerUserProfile() {
        //todo
		return true;
	}
	
	public void addFriend(User from, User friend) {
		if(!this.userFriends.containsKey(from)) {
			this.userFriends.put(from, new ArrayList<User>());
		}
		this.userFriends.get(from).add(friend);
	}
	
	public boolean userLoginAuth() {
        //todo
		return true;
	}
	
	public void addUser(User fromUser, String toAccountName) {
		User toUser = usersByAccountName.get(toAccountName);
		AddRequest req = new AddRequest(fromUser, toUser, new Date());
		toUser.receivedAddRequest(req);
		fromUser.sentAddRequest(req);
	}
	
	public void approveAddRequest(AddRequest req) {
		req.status = RequestStatus.ACCEPTED;
		User from = req.getFromUser();
		User to = req.getToUser();
		from.addContact(to);
		to.addContact(from);
        addFriend(from, to);
        addFriend(to, from);
	}
	
	public void rejectAddRequest(AddRequest req) {
		req.status = RequestStatus.REJECTED;
		User from = req.getFromUser();
		User to = req.getToUser();
		from.removeAddRequest(req);
		to.removeAddRequest(req);		
	}
	
	public void userSignedOn(String accountName) {
		User user = usersByAccountName.get(accountName);
		if (user != null) {
			user.setStatus(UserStatusType.ONLINE);			
			onlineUsers.put(user.getId(), user);
		}
	}
	
	public void userSignedOff(String accountName) {
		User user = usersByAccountName.get(accountName);
		if (user != null) {
			user.setStatus(UserStatusType.OFFLINE);
			onlineUsers.remove(user.getId());
		}
	}	
	
}


// Client

class User {
	private int id;
	private UserStatusType status = null;
	private HashMap<Integer, PrivateChat> privateChats = new HashMap<Integer, PrivateChat>();
	private ArrayList<GroupChat> groupChats = new ArrayList<GroupChat>();
	private HashMap<Integer, AddRequest> receivedAddRequests = new HashMap<Integer, AddRequest>();
	private HashMap<Integer, AddRequest> sentAddRequests = new HashMap<Integer, AddRequest>();
	private HashMap<Integer, User> contacts = new HashMap<Integer, User>();
	private String accountName;
	private String fullName;
	
	public User(int id, String accountName, String fullName) {
		
	}
	
	public boolean sendMessageToUser(User toUser, String content) {
		PrivateChat chat = privateChats.get(toUser.getId());
		if (chat == null) {
			chat = new PrivateChat(this, toUser);
			privateChats.put(toUser.getId(), chat);
		}
		Message message = new Message(content, new Date());
		return chat.addMessage(message);
	}
	
	public boolean sendMessageToGroupChat(int groupId, String content) {
		GroupChat chat = groupChats.get(groupId);
		if (chat != null) {
			Message message = new Message(content, new Date());
			return chat.addMessage(message);
		}
		return false;
	}
	
	public void setStatus(UserStatusType status) {
		this.status = status;
	}
	
	public UserStatusType getStatus() {
		return status;
	}
	
	public boolean addContact(User user) {
		if (contacts.containsKey(user.getId())) {
			return false;
		} else {
			contacts.put(user.getId(), user);
			return true;
		}
	}
	
	public void receivedAddRequest(AddRequest req) {
		int senderId = req.getFromUser().getId();
		if (!receivedAddRequests.containsKey(senderId)) {
			receivedAddRequests.put(senderId, req);
		}		
	}
	
	public void sentAddRequest(AddRequest req) {
		int receiverId = req.getFromUser().getId();
		if (!sentAddRequests.containsKey(receiverId)) {
			sentAddRequests.put(receiverId, req);
		}		
	}
	
	public void removeAddRequest(AddRequest req) {
		if (req.getToUser() == this) {
			receivedAddRequests.remove(req);
		} else if (req.getFromUser() == this) {
			sentAddRequests.remove(req);
		}
	}
	
	public void requestAddUser(String accountName) {
		Server.getInstance().addUser(this, accountName);
	}
	
	public void addConversation(PrivateChat conversation) {
		User otherUser = conversation.getOtherParticipant(this);
		privateChats.put(otherUser.getId(), conversation);
	}

	public void addConversation(GroupChat conversation) {
		groupChats.add(conversation);
	}	
	
	public int getId() {
		return id;
	}
	
	public String getAccountName() {
		return accountName;
	}
	
	public String getFullName() {
		return fullName;
	}
}

class Message {
	private String message;
	private Date date;
	
	public Message(String message, Date date) {
		this.message = message;
		this.date = date;
	}
	
	public String getContent() {
		return this.message;
	}
	
	public Date getDate() {
		return this.date;
	}
	

}

abstract class Conversation {
	protected ArrayList<User> participants = new ArrayList<User>();
	protected ArrayList<Message> messages = new ArrayList<Message>();
	protected int id;
	
	public ArrayList<Message> getMessages(){
		return messages;
	}
	
	public boolean addMessage(Message m) {
		this.messages.add(m);
		return true;
	}
	
	public int getId() {
		return this.id;
	}
}

class PrivateChat extends Conversation {
	public PrivateChat(User u1, User u2) {
		participants.add(u1);
		participants.add(u2);
	}
	
	public User getOtherParticipant(User primary) {
		if(participants.get(0) == primary) {
			return participants.get(1);
		}
		else {
			return participants.get(0);
		}
	}
}

class GroupChat extends Conversation {
	public void removeParticipant(User user) {
		participants.remove(user);
	}
	
	public void addParticipant(User user) {
		participants.add(user);
	}
}