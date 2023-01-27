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
    //data2 is the same but always 50
    let data2 = generate_data(240, 5).map(() => 50);

    onMount(() => { 
		new Chart(ctx, {
			type: 'line',
			data: {
				labels: labels,
				datasets: [
					{
						label: 'Current',
                        data: data,
                        borderWidth: 1,
                        backgroundColor: 'rgb(255, 133, 133)',
                        borderColor: 'rgb(255, 133, 133)',
                    },
                    {
                        label: 'Target',
                        data: data2,
                        borderWidth: 1,
                        backgroundColor: 'rgb(98, 203, 118)',
                        borderColor: 'rgb(114, 234, 137)',
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