import java.util.*;
public class Person{
    String id;
    private String name;
    ArrayList<String> friends;
    public Person(String name){
        this.id = UUID.randomUUID().toString(); // use unique ID gen for this
        this.name = name;
        this.friends = new ArrayList<>();
    }

}
public class PersonServer{
    String id;
    HashMap<String, Person> people;

    public void addPerson(Person p){
        this.people.put(p.id, p);
    }

    public ArrayList<Person> getPeople(int[] ids){
        ArrayList<Person> result = new ArrayList<Person>();
        for(int i =0; i<ids.length; i++){
            result.add(this.people.get(ids[i]));
        }
        return result;
    }
}

public class LookupService{
    HashMap<String, PersonServer> lookup;
    public PersonServer lookuPersonServer(String personId){
        return this.lookup.get(personId);
    }

}

public class GraphService{
    LookupService lookupService = new LookupService();

    public Person getPerson(String id){
        PersonServer p = lookupService.lookuPersonServer(id);
        return p.people.get(id);
    }

    public ArrayList<String> shortestPath(String source, String dest){
        if(source == null || dest == null) return null;
        HashMap<String, String> prevNodeKeys = shortestPathHelper(source, dest);
        if(prevNodeKeys!=null){
            ArrayList<String> path = new ArrayList<>();
            String prev = prevNodeKeys.get(dest);
            while(prev!="0"){
                path.add(prev);
                prev = prevNodeKeys.get(prev);
            }
            return Collections.reverse(path);
        }
    }
    public HashMap<String, String> shortestPathHelper(String source_key, String dest_key){
        Person source = getPerson(source_key);
        Person dest = getPerson(dest_key);
        Queue<Person> queue = new LinkedList<>();
        queue.add(source);
        HashMap<String, String> prevNodeKeys = new HashMap<String, String>();
        prevNodeKeys.put(source_key, "0");
        Set<String> visited = new HashSet<String>();

        while(queue.size()!=0){
            Person node = queue.poll();
            if(node.id == dest_key){
                return prevNodeKeys;
            }
            Person prev= node;
            for(String f: node.friends){
                if(!visited.contains(f)){
                    Person friend = getPerson(f);
                    queue.add(friend);
                    prevNodeKeys.put(f, friend.id);
                    visited.add(f);
                }
            }

        }
        return null;
    }

}