from utils import plt, np, get_output_path

 
def add_noise(base, noise_level):
    return base + rng.normal(loc=0, scale=noise_level, size=len(base))


fig, axs = plt.subplots(3, 1, figsize=(6, 7.5), sharex=True, sharey=True)
fig.set_layout_engine('tight')
periods = np.arange(1, 13)
rng = np.random.default_rng(19)

y_ideal_base = np.full_like(periods, 0.8, dtype=float)
y_ideal = add_noise(y_ideal_base, 0.005)
axs[0].set_title('Ideal', weight='bold')
axs[0].plot(periods, y_ideal_base, color='steelblue')
axs[0].scatter(periods, y_ideal, color='black', marker='x')

y_fall_base = np.linspace(0.9, 0.2, len(periods))
y_fall_small = add_noise(y_fall_base, 0.03)
axs[1].set_title('Predictable Fall', weight='bold')
axs[1].plot(periods, y_fall_base, color='steelblue')
axs[1].scatter(periods, y_fall_small, color='black', marker='x')

y_trend = np.linspace(0.9, 0.3, len(periods))
y_noisy = add_noise(y_trend, 0.15)
axs[2].set_title('Unpredictable Fall', weight='bold')
axs[2].plot(periods, y_trend, color='steelblue')
axs[2].scatter(periods, y_noisy, color='black', marker='x')

for ax in axs:
    ax.set_ylabel("Eval Metric")
    ax.grid(linestyle='--', color='lightgray')
    ax.spines[['top', 'right']].set_visible(False)
    ax.set_ylim(0, 1)
    ax.set_yticks(np.arange(0, 1.1, 0.2))
axs[-1].set_xlabel("Period")

fig.savefig(get_output_path('stability_patterns.png'), dpi=100)