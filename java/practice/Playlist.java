import java.util.ArrayList;

class Playlist
{
  public static void main(String[] args)
  {
    ArrayList<String> desertIslandPlaylist = new ArrayList<String>();

     desertIslandPlaylist.add("Yummy");
     desertIslandPlaylist.add("TGIF");
     desertIslandPlaylist.add("I like me better");
     desertIslandPlaylist.add("Nver Again");
     desertIslandPlaylist.add("however i do");
     desertIslandPlaylist.add("mine");

     System.out.println(desertIslandPlaylist.size());
     desertIslandPlaylist.remove(4);

     //switch the places of the first and second song
     String a = desertIslandPlaylist.get(0);
     String b = desertIslandPlaylist.get(1);
     desertIslandPlaylist.set(1, a);
     desertIslandPlaylist.set(0,b);
     desertIslandPlaylist.indexOf()


     System.out.println(desertIslandPlaylist);
  }
}
