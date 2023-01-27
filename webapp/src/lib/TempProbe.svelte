<script lang="ts">
    import { onMount } from 'svelte';
    import Chart from 'chart.js/auto';
	let ctx: any;

    function generate_labels(seconds: number, interval: number) {
        let labels = [];
        for (let i = 0; i < seconds; i += interval) {
            labels.push(i);
        }
        //invert the array
        labels.reverse();
        return labels;
    }

    function generate_data(seconds: number, interval: number) {
        let data = [];
        for (let i = 0; i < seconds; i += interval) {
            data.push(Math.random() * 100);
        }
        //invert the array
        data.reverse();
        return data;
    }

    let labels = generate_labels(240, 5);
    let data = generate_data(240, 5);
    let data2 = generate_data(240, 5);

    onMount(() => { 
		new Chart(ctx, {
			type: 'line',
			data: {
				labels: labels,
				datasets: [
					{
						label: 'Current',
                        data: data,
                        borderWidth: 1
                    },
                    {
                        label: 'Target',
                        data: data2,
                        borderWidth: 1
                    }
				]
			},
			options: {
				scales: {
					y: {
						beginAtZero: true
					}
				}
			}
		});
		
	});
</script>

<canvas bind:this={ctx}/>