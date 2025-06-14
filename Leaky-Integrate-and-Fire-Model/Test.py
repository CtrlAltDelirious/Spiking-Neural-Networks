import brian2 as b2
from Spiking-Neural-Networks.Leaky-Integrate-and-Fire-Model import Main
from Spiking-Neural-Networks.tools import input_factory

print("resting potential: {}".format(Leaky-Integrate-and-Fire-Model.V_REST))

# create a step current with amplitude = I_min
step_current = input_factory.get_step_current(
    t_start=5, t_end=100, unit_time=b2.ms,
    amplitude=I_min)  # set I_min to your value

# run the LIF model.
# Note: As we do not specify any model parameters, the simulation runs with the default values
(state_monitor,spike_monitor) = Leaky-Integrate-and-Fire-Model.simulate_LIF_neuron(input_current=step_current, simulation_time = 100 * b2.ms)

# plot I and vm
plot_tools.plot_voltage_and_current_traces(
state_monitor, step_current, title="min input", firing_threshold=LIF.FIRING_THRESHOLD)
print("nr of spikes: {}".format(spike_monitor.count[0]))  # should be 0
