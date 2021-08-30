import cProfile
import idilioatomico

pr = cProfile.Profile()
pr.enable()
pr.run('idilioatomico.make("F",20)')
pr.disable()
pr.print_stats(sort='ncalls')