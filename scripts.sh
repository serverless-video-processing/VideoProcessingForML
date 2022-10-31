# Profiling using cProfile
python3 -m cProfile -o ./data/profile.pstats process.py
# Visualise pstats file
gprof2dot -f pstats --root=process_oop:31:pipeline ./data/profile.pstats | dot -Tpng -o ./viz/gprof2dot.png

# Profiling Memory Usage
mprof run --python python3 process_oop.py
python3 -m memory_profiler process_oop.py