NGAO SIMULATOR 
NGAO Simulator tries different card combinations to find the best possible hand for a player.

Rules:
+------------+  
1st Round  
+------------+  
Each player gets 3 cards, the player with highest points wins the 1st round.  
Some Example:   
```
+------+  +------+  +------+  
| 2    |  | 5    |  | 6    |  
|  ♠   |  |  ♣   |  |  ♠   |  
|   2  |  |   5  |  |   6  |  
+------+  +------+  +------+  (2 + 5 + 6 = 13) ~ 3 points

+------+  +------+  +------+  
| 3    |  | 7    |  | 9    |  
|  ♣   |  |  ♠   |  |  ♠   |  
|   3  |  |   7  |  |   9  |  
+------+  +------+  +------+  (3 + 7 + 9 = 19) ~ 9 points
```

+-----------------------------------------------------------------+  
Reward for 1st round:  
1 - 9 points - reward X 1  
10 points - reward X 2  
3 cards composed of any "J", "Q", "K" - reward X 3  
Same cards (eg: 3,3,3 | 4,4,4 | J,J,J) - reward X 5  
+-----------------------------------------------------------------+  

+----------+  
2nd Round  
+----------+  
Each player will get 2 additional cards.  
Player must use 3 cards to form a valid base (base is any 3 cards that sum up to 10,20 or 30)  
Card with number "3" can represent "6" and vice versa  
```
+------+  +------+  +------+  
| J    |  | K    |  | K    |  
|  ♦   |  |  ♣   |  |  ♥   |  
|   J  |  |   K  |  |   K  |  
+------+  +------+  +------+  --> valid base

+------+  +------+  +------+  
| 5    |  | J    |  | K    |  
|  ♥   |  |  ♦   |  |  ♣   |  
|   5  |  |   J  |  |   K  |  
+------+  +------+  +------+  --> invalid base
```

Some Example:  
```
    +------+  +------+  
    | 7    |  | 8    |  
    |  ♣   |  |  ♠   |  
    |   7  |  |   8  |  
    +------+  +------+  
+------+  +------+  +------+  
| K    |  | Q    |  | J    |  
|  ♠   |  |  ♥   |  |  ♥   |  
|   K  |  |   Q  |  |   J  |  
+------+  +------+  +------+  --> 5 points


    +------+  +------+  
    | 3    |  | 3    |  
    |  ♦   |  |  ♥   |  
    |   3  |  |   3  |  
    +------+  +------+  
+------+  +------+  +------+  
| 8    |  | 9    |  | 6    |  
|  ♦   |  |  ♣   |  |  ♦   |  
|   8  |  |   9  |  |   6  |  
+------+  +------+  +------+
(how does 8 + 9 + 6 = 23 form a valid base? Remember: "6" can represent "3"


+------+  +------+  +------+  +------+  +------+  
| 7    |  | J    |  | K    |  | 2    |  | 9    |  
|  ♦   |  |  ♠   |  |  ♥   |  |  ♦   |  |  ♦   |  
|   7  |  |   J  |  |   K  |  |   2  |  |   9  |  
+------+  +------+  +------+  +------+  +------+
if these are your cards, (congratulation you have the worst possible hand) because you can't form a valid base

```
+-----------------------------------------------------------------+  
Reward for 2nd round:  
Sum of Top cards with 1 - 9 points - Reward X 1  
Sum of Top cards with 10 points - Reward X 2  
Same top cards (example 2) - Reward X 3  
Top cards with Ace of spades and any "J", "Q", "K" - Reward X 5  

eg:
```
    +------+  +------+  
    | A    |  | K    |  
    |  ♠   |  |  ♥   |  
    |   A  |  |   K  |  
    +------+  +------+  
+------+  +------+  +------+  
| 8    |  | 9    |  | 6    |  
|  ♦   |  |  ♣   |  |  ♦   |  
|   8  |  |   9  |  |   6  |  
+------+  +------+  +------+
```
+-----------------------------------------------------------------+

