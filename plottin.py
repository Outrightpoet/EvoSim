import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np
import gc

def plot_data(data1, title1, data2, title2, lines_data, x, line_labels=None, title3="Species Population", topn_dict=None, n_top=5, species=None):


    #for amount of breaking you want your computer to do
    breaking1 = True
    breaking2 = True
    breaking3 = True
    breaking4 = True
    breaking5 = True
    breaking6 = True

    fig, axes = plt.subplots(3, 2, figsize=(12, 12))

    # --- Top row: heatmaps ---
    if breaking1 == True:
        colors = ['cyan', 'lightgreen', 'green', 'gray', 'darkkhaki', 'yellow']
        cmap = ListedColormap(colors)

        im1 = axes[0, 0].imshow(data1, cmap=cmap, interpolation='nearest')
        axes[0, 0].set_title(title1)
        plt.colorbar(im1, ax=axes[0, 0])

    if breaking2 == True:
        im2 = axes[0, 1].imshow(data2, cmap='viridis', interpolation='nearest')
        axes[0, 1].set_title(title2)
        plt.colorbar(im2, ax=axes[0, 1])

    # --- Bottom-left: line plot ---
    if breaking3 == True:
        ax_line = axes[1, 0]
        # Remove bottom-right axes if we don't want to overwrite
        if topn_dict is None:
            fig.delaxes(axes[1, 1])

        # Plot each line
        for i, y in enumerate(lines_data.values()):
            ax_line.plot(x, y, marker='o')

        ax_line.set_title(title3)
        ax_line.set_xlabel("Years")
        ax_line.set_ylabel("Population")
        ax_line.grid(True)

    # --- Bottom-right: top-N bar chart ---
    if breaking4 == True:
        ax_bar = axes[1, 1]

        # Sort dict items descending
        sorted_items = sorted(topn_dict.items(), key=lambda item: item[1], reverse=True)[:n_top]
        names = [item[0] for item in sorted_items]
        values = [item[1] for item in sorted_items]

        # Highlight top value
        colors = ['red'] + ['skyblue'] * (len(values) - 1)

        ax_bar.barh(names, values, color=colors)
        ax_bar.set_xlabel("Population")
        ax_bar.set_ylabel("Name")
        ax_bar.set_title("Top Pop Species")
        ax_bar.invert_yaxis()  # top value on top

    if breaking5 == True and len(species) != 1:
        fig.delaxes(axes[2, 0])  # remove the original Cartesian subplot
        ax_spider = plt.subplot(3, 2, 5, polar=True)

        # Make the subplot polar
        ax_spider = axes[2, 0]
        ax_spider = plt.subplot(3, 2, 5, polar=True)  # override with polar axes

        # Get the top-N items
        sorted_items = sorted(topn_dict.items(), key=lambda item: item[1], reverse=True)[:n_top]

        # Define labels (five axes)
        labels = [
            'Diet Scale',
            'Diet Range',
            'Defensive Spikes',
            'Size',
            'Claws',
            'Sharp Teeth',
            'Thick Skin',
            'Bone Plates',
            'Scales',
            'Tail',
            'Club Tail',
            'Horns',
            'Webbed Feet',
            'Hoofs',
            'Soft Feet',
            'Hearing',
            'Camouflage',
            'Sight',
            'Long Legs',
            'Dense Muscles'
        ]

        num_vars = len(labels)
        angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
        angles += angles[:1]  # close the loop

        # Plot each creature
        for name in sorted_items:
            name1 = name[0]
            values = [
                species[name1][2][list(species[name1][2])[0]].traits.diet_scale,
                species[name1][2][list(species[name1][2])[0]].traits.diet_range,
                species[name1][2][list(species[name1][2])[0]].traits.defensive_spikes,
                species[name1][2][list(species[name1][2])[0]].traits.size,
                species[name1][2][list(species[name1][2])[0]].traits.claws,
                species[name1][2][list(species[name1][2])[0]].traits.sharp_teeth,
                species[name1][2][list(species[name1][2])[0]].traits.thick_skin,
                species[name1][2][list(species[name1][2])[0]].traits.bone_plates,
                species[name1][2][list(species[name1][2])[0]].traits.scales,
                species[name1][2][list(species[name1][2])[0]].traits.tail,
                species[name1][2][list(species[name1][2])[0]].traits.club_tail,
                species[name1][2][list(species[name1][2])[0]].traits.horns,
                species[name1][2][list(species[name1][2])[0]].traits.webbed_feet,
                species[name1][2][list(species[name1][2])[0]].traits.hoofs,
                species[name1][2][list(species[name1][2])[0]].traits.soft_feet,
                species[name1][2][list(species[name1][2])[0]].traits.hearing,
                species[name1][2][list(species[name1][2])[0]].traits.camouflage,
                species[name1][2][list(species[name1][2])[0]].traits.sight,
                species[name1][2][list(species[name1][2])[0]].traits.long_legs,
                species[name1][2][list(species[name1][2])[0]].traits.dense_muscles,
            ]

            values += values[:1]  # close the loop

            ax_spider.plot(angles, values, linewidth=2, label=name1)
            ax_spider.fill(angles, values, alpha=0.1)

        ax_spider.set_xticks(angles[:-1])
        ax_spider.set_xticklabels(labels)
        ax_spider.set_yticklabels([])  # hide radial labels
        ax_spider.set_ylim(0, 100)
        ax_spider.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1))
        ax_spider.set_title("Top Five Species Traits")

    if breaking6 == True and len(species) != 1:
        fig.delaxes(axes[2, 1])  # remove the original Cartesian subplot
        ax_spider = plt.subplot(3, 2, 5, polar=True)

        # Make the subplot polar
        ax_spider = axes[2, 1]
        ax_spider = plt.subplot(3, 2, 6, polar=True)

        # Get the top-N items
        sorted_items = sorted(topn_dict.items(), key=lambda item: item[1], reverse=True)

        # Define labels (five axes)
        labels = [
            'Diet Scale',
            'Diet Range',
            'Defensive Spikes',
            'Size',
            'Claws',
            'Sharp Teeth',
            'Thick Skin',
            'Bone Plates',
            'Scales',
            'Tail',
            'Club Tail',
            'Horns',
            'Webbed Feet',
            'Hoofs',
            'Soft Feet',
            'Hearing',
            'Camouflage',
            'Sight',
            'Long Legs',
            'Dense Muscles'
        ]

        num_vars = len(labels)
        angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
        angles += angles[:1]  # close the loop

        values = [0] * 20


        # Plot each creature
        for name in sorted_items:
            name1 = name[0]
            values_temp = [
                species[name1][2][list(species[name1][2])[0]].traits.diet_scale,
                species[name1][2][list(species[name1][2])[0]].traits.diet_range,
                species[name1][2][list(species[name1][2])[0]].traits.defensive_spikes,
                species[name1][2][list(species[name1][2])[0]].traits.size,
                species[name1][2][list(species[name1][2])[0]].traits.claws,
                species[name1][2][list(species[name1][2])[0]].traits.sharp_teeth,
                species[name1][2][list(species[name1][2])[0]].traits.thick_skin,
                species[name1][2][list(species[name1][2])[0]].traits.bone_plates,
                species[name1][2][list(species[name1][2])[0]].traits.scales,
                species[name1][2][list(species[name1][2])[0]].traits.tail,
                species[name1][2][list(species[name1][2])[0]].traits.club_tail,
                species[name1][2][list(species[name1][2])[0]].traits.horns,
                species[name1][2][list(species[name1][2])[0]].traits.webbed_feet,
                species[name1][2][list(species[name1][2])[0]].traits.hoofs,
                species[name1][2][list(species[name1][2])[0]].traits.soft_feet,
                species[name1][2][list(species[name1][2])[0]].traits.hearing,
                species[name1][2][list(species[name1][2])[0]].traits.camouflage,
                species[name1][2][list(species[name1][2])[0]].traits.sight,
                species[name1][2][list(species[name1][2])[0]].traits.long_legs,
                species[name1][2][list(species[name1][2])[0]].traits.dense_muscles,
            ]


            values_temp += values_temp[:1]  # close the loop

            for i in range(0, len(values)):
                try:
                    values[i] += int(values_temp[i])
                except IndexError:
                    pass


        for i in range(0,len(values)):
            values[i] = values[i] / len(sorted_items)


        values.append(values[0])

        ax_spider.plot(angles, values, linewidth=2, label="average")
        ax_spider.fill(angles, values, alpha=0.1)

        ax_spider.set_xticks(angles[:-1])
        ax_spider.set_xticklabels(labels)
        ax_spider.set_yticklabels([])  # hide radial labels
        ax_spider.set_ylim(0, 100)
        ax_spider.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1))
        ax_spider.set_title("Average Species Traits")

    if breaking1 or breaking2 or breaking3 or breaking4 or breaking5 or breaking6:
        if not hasattr(plot_data, "fig"):
            # first run, create figure and show
            plt.tight_layout()
            plt.show(block=False)
        else:
            # subsequent runs, just update/redraw
            plot_data.fig.canvas.draw_idle()
            plot_data.fig.canvas.flush_events()



