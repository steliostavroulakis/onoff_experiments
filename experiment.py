import coba as cb

from learners import RandomSetLearner
from environments import MathEnvironment

env = cb.Environments(MathEnvironment(8)).take(10)
lrn = [RandomSetLearner(1)]

cb.Experiment(env,lrn).run().plot_learners()
