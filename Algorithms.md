## Sortering

* ### Sammenligningsbasert sortering
  * ### Merge sort
    * **Stabil**
    * **Ikke** in-place
    * Rutime:

      Best|Average|Worst
      :-:|:-:|:-:
      Ω(n log(n)) | Θ(n log(n)) | O(n log(n))
      </br>
  * ### Quicksort
    * **Ikke** Stabil
    * **in-place**
    * Rutime:
  
      Best|Average|Worst
      :-:|:-:|:-:
      Ω(n log(n)) | Θ(n log(n)) | O(n<sup>2</sup>)
      </br>
  * ### Insertion sort
    * **Stabil**
    * **in-place**
    * Rutime:

      Best|Average|Worst
      :-:|:-:|:-:
      Ω(n) | Θ(n<sup>2</sup>) | O(n<sup>2</sup>)
      </br>
  * Heap sort
    * **Ikke** Stabil
    * **in-place**
    * Rutime:
      Best|Average|Worst
      :-:|:-:|:-:
      Ω(n log(n)) | Θ(n log(n)) | O(n log(n))

</br>

* ### IKKE-sammenligningsbasert sortering
  * Counting sort
    * **Stabil**
    * **Ikke** in-place
    * Rutime:

      Best|Average|Worst
      :-:|:-:|:-:
      Ω(n+k) | Θ(n+k) | O(n+k)
      </br>
  * Radix sort
    * **Stabil***
    * **Ikke** in-place
    * Rutime:

      Best|Average|Worst
      :-:|:-:|:-:
      Ω(d(n+k)) | Θ(d(n+k)) | O(d(n+k))
      </br>
  * Bucket sort
    * **Stabil**
    * **Ikke** in-place
    * Rutime:

      Best|Average|Worst
      :-:|:-:|:-:
      Ω(n) | Θ(n) | O(n<sup>2</sup>)
      </br>

## Heaps
* ### Max-Heapify
  * Rutime: O(lg n)
    </br>
* ### Heapsort
  * Rutime: O(lg n)
    </br>

<!--  
Huffmann-koder
BFS
DFS
Topologisk sortering
Kruskal's algoritme
Prim's algoritme
Bellman-ford
Dag-shortest path
Dijkstra's algoritme
Floyd-Warshall
Ford-Fulkerson-metoden
Edmonds-Karp
johnson's algorithm
-->