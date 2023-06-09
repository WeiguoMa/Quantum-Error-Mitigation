"""
Author: weiguo_ma
Time: 04.30.2023
Contact: weiguo.m@iphy.ac.cn
"""
import tensornetwork as tn

import Library.tools as tools
from Library.ADCircuits import TensorCircuit
from Library.AbstractGate import AbstractGate

# # Ignore warnings from tensornetwork package when using pytorch backend for svd
# warnings.filterwarnings("ignore")
# # Bugs fixed in tensornetwork package, which is 'torch.svd, torch.qr' -> 'torch.linalg.svd, torch.linalg.qr'

tn.set_default_backend("pytorch")

# Basic information of circuit
qnumber = 4
ideal_circuit = False   # or True
realNoise = True		# or False
chiFilename = './data/chi/chi1.mat'
chi, kappa = None, None

# Establish a quantum circuit
circuit = TensorCircuit(ideal=ideal_circuit, realNoise=realNoise,
                        chiFilename=chiFilename, chi=chi, kappa=kappa)

circuit.add_gate(AbstractGate().h(), [0])
circuit.add_gate(AbstractGate().cnot(), [0, 1])
circuit.add_gate(AbstractGate().cnot(), [1, 2])
circuit.add_gate(AbstractGate().cnot(), [2, 3])

print(circuit)


# Generate an initial quantum state
state = tools.create_ket0Series(qnumber)
state = circuit(state, state_vector=False, reduced_index=[])

# Calculate probability distribution
prob_dict = tools.density2prob(state, tolerant=5e-4)

# plot probability distribution
tools.plot_histogram(prob_dict, title='Probability Distribution')