# Diffusion Limited Aggregation (DLA) System 

Parametric, Computational Design mini Project

## intro
DLA는 눈 결정의 현미경 사진을 통해 가장 쉽게 관측할 수 있는 자연적인 패턴의 한가지입니다. <br> 
공기나 유체상을 자유롭게 부유하는 독립 적인 입자들이 특정 거리안으로 가까워졌을 때 서로의 인력에 의하여 결합되어 하나의 큰 입자를 생성하며 이러한 입자는 또 다른 부유입자를 연속적으로 끌어당김으로써 나무가지 를 위에서 바라본 것과 같은 패턴을 생성하게 됩니다.

<br>

### What is Diffusion-Limited Aggregation ?
브라운 운동으로 인해 임의운동을 하는 입자들이 서로 뭉쳐서 입자들의 집합체를 형성하는 과정 (위키백과에서 발췌). 이 과정은 크게 두 가지로 나눌 수 있습니다.

- **Diffusion (Wandering Particle)** <br> : 두 점으로 시작합니다. 하나는 끌어당기는 역할을 하는 상태 (static working as an atteractor) 이며, 다른 하나는 시간이 지남에 따라 끌어당기는 쪽으로 서서히 접근하는 방황하는 파티클 Wandering particle 입니다.
![image]()

- **Aggregation (Sticking Particles within threshold)** <br> : 두 지점이 충분히 가까운지 지속적으로 확인한다. 임계값Threshold에 도달하면 방황을 멈추고 두 점을 하나의 선으로 연결하여 병합, 그렇지 않으면 파티클Particles이 임계값에 도달할 때까지 계속 방황하도록 놓아둔다.
![image]()

<br>


### Process

**step 01** <br>
Get a random point on a given boundary. This point will gradually approach to an attractor as it wander within the boundary. The attractor will be the first aggregate as it still serve as an attractor.
![image]()

**step 02** <br>
When wandering a particle, keep the random angle less than 180 degrees to force the particle move toward the attractor. Otherwise, the particle might be lost in the space.
![image]()

**step 03** <br>
Every time moving the particle, check the distance between the two points to see if they are close enough to get merged. 
![image]()

**step 04** <br>
If they are not close enough, then keep the particle wandering. 
![image]()

**step 05** <br>
If yes, merge two points, connecting them with a single line. Two points form a new set of aggregate. 
![image]()

**step 06** <br>
Get another random point on the boundary and get it wander.
![image]()

**step 07** <br>
Check distance from the wandering particle to each aggregate every time the particle moves. If any of the two distance is within the threshold, merge the particle to the nearer aggregate. If none of the two meets the condition, keep it wandering.
![image]()

**step 08** <br>
Repeat until you like the pattern.
![image]()
