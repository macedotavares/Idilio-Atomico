import cProfile
import idilioatomico

pr = cProfile.Profile()
pr.enable()
pr.run('idilioatomico.make("F",10000)')
pr.disable()
pr.print_stats(sort='cumtime')