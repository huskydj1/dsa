import java.io.*;
import java.util.*;

class Pair implements Comparable<Pair>{
    int x;
    int v;
    int w;
    Pair(int a, int n, int p){ // New Instance
        x=a;
        v=n;
        w=p;
    }
    public String toString() { // Printing Edge Information
        return x + " " + v + " " + w;
    }
    public int compareTo(Pair o) { // Sorting by Weight
        return this.w-o.w;
    }
}

public class TestingPrim {
    public static int n, m; // Number of nodes, number of edges
    public static ArrayList<Pair> a[]; // Adjacency List
    public static int cost = 0; // MST Cost
    public static boolean visited[]; //Visited Array

    public static void main(String[] args) {
        // Main Function, Running All Code
        ini();
        System.out.println("Stored Graph: " + Arrays.toString(a));
        int start = 1; // Starting Node doesn't matter
        run(start);
        System.out.println(cost); // The MST Cost
    }

    static void run(int start) {
        PriorityQueue<Pair> q = new PriorityQueue<Pair>();
        q.add(new Pair(start, start,0));

        int current = start;

        // Go through priority queue with edges
        while(!q.isEmpty()) {
            // Next Node
            assert(!q.isEmpty());
            int here = q.peek().x;
            int go = q.peek().v;
            int dis = q.peek().w;
            q.poll();

            assert(0<=go && go<visited.length);
            if(visited[go]) continue;
            if(here!=current) {
                // Relaxing

                assert(!q.isEmpty());
                Pair temp = q.poll();
                q.add(new Pair(here, go, dis));
                here = temp.x;
                go = temp.v;
                dis = temp.w;
            }


            cost+=dis;
            System.out.println(current + " " + go + " " + cost);
            current = go;
            visited[go]=true;

            for(int i = 0; i<a[go].size(); i++) {
                if(!visited[a[go].get(i).v]) {
                    q.add(a[go].get(i));
                }
            }

        }
    }

    static void ini() {
        Scanner in = new Scanner(System.in);
        n = in.nextInt();
        m = in.nextInt();

        // Instantiate new Adjacency List
        a = new ArrayList[n+1];
        visited = new boolean[n+1];
        for(int i = 1; i<=n; i++) {
            a[i] = new ArrayList<Pair>();
        }

        // Add Edges to Adjacency List
        for(int i = 0; i<m; i++) {
            int x = in.nextInt();
            int y = in.nextInt();
            int z = in.nextInt();
            a[x].add(new Pair(x, y,z));
            a[y].add(new Pair(y, x,z));
        }
        in.close();
    }
}

/*
7 11 
1 7 12
1 4 28
1 2 67
1 5 17
2 4 24
2 5 62
3 5 20
3 6 37
4 7 13
5 6 45
5 7 73

6 9
1 2 5
1 3 4
2 3 2
2 4 7
3 4 6
3 5 11
4 5 3
4 6 8
5 6 8
*/