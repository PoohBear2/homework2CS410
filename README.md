# Task 4:
I am convinced after Thanos’s Eureka moment from results in figure 3. This is because alpha-beta pruning expanded fewer states than Minimax to achieve better if not similar results. Consider the performance for depth=4. Alpha Beta (the purple square) expanded <25,000 states while minimax (the purple circle) expanded roughly 35,000 states to arrive at a same rough performance score of 420. While minimax did outperform alpha beta for depth 3, minimax only did so by a very marginal amount while expanding what qualitatively seems to be over 50,000 more states. This indicates that Thanos’s 2nd experiment showed how minimax had an inefficient tradeoff between states expanded and performance. As further evidenced by depth = 2 and depth = 1, alpha beta expanded fewer states while performing at a level comparable to minimax, all supporting how alpha-beta runs faster while being more reliable. I am even more convinced after accounting for the information in figure 2. Whenever alpha beta explored further in the tree than minimax, it performed better (generally + as expected). When the cutoff depth for alpha beta is the same as the cut off depth for minimax, both agents roughly won and lost an equal number of games with each other. Whenever minimax expired further in the tree than alpha beta, it performed better (generally + as expected). However, by expanding fewer states than minimax to achieve similar results if not an overwhelming superiority when it has a larger or equal cutoff depth as minimax, alpha beta is more efficient and better. Thanos convinced me!

# Tests:
I tested the if the end result is good and if the number of states expanded is correct for both alpha-beta and minimax 
