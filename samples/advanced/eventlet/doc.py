#-*-codingutf-8 -*-
"""
eventlet语境下的“绿色线程”普通线程之间的区别：
　　1. 绿色线程几乎没有开销，不用像保留普通线程一样保留“绿色线程”，每一个网络连接对应至少一个“绿色线程”；
　　2. 绿色线程需要人为的设置使其互相让渡CPU控制权，而不是抢占。绿色线程既能够共享数据结构，又不需要显式的互斥控制，
       因为只有当一个绿色线程让出了控制权后其他的绿色线程才能访问彼此共享的数据结构。

下图是eventlet中协程、hub、线程、进程之间的关系：
 _______________________________________
| python process                        |
|   _________________________________   |
|  | python thread                   |  |
|  |   _____   ___________________   |  |
|  |  | hub | | pool              |  |  |
|  |  |_____| |   _____________   |  |  |
|  |          |  | greenthread |  |  |  |
|  |          |  |_____________|  |  |  |
|  |          |   _____________   |  |  |
|  |          |  | greenthread |  |  |  |
|  |          |  |_____________|  |  |  |
|  |          |   _____________   |  |  |
|  |          |  | greenthread |  |  |  |
|  |          |  |_____________|  |  |  |
|  |          |                   |  |  |
|  |          |        ...        |  |  |
|  |          |___________________|  |  |
|  |                                 |  |
|  |_________________________________|  |
|                                       |
|   _________________________________   |
|  | python thread                   |  |
|  |_________________________________|  |
|   _________________________________   |
|  | python thread                   |  |
|  |_________________________________|  |
|                                       |
|                 ...                   |
|_______________________________________|

绿色线程是线程内的概念，同一个线程内的绿色线程之间是顺序执行的，绿色线程之间想要实现同步，
 需要开发人员在阻塞的代码位置显式植入CPU让渡，此时hub接管进行调度，寻找同一个线程内另一个可调度的绿色线程。
 注意绿色线程是线程内的概念，不能跨线程同步。
"""