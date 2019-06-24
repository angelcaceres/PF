from ising import IsingLattice
lattice = IsingLattice(tempature=.50, initial_state="r", size=(100,100))
lattice.run(video=True)