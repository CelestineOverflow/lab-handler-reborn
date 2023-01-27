<script lang="ts">
    import type monaco from 'monaco-editor';
    import { onMount } from 'svelte';
                    
    let divEl: HTMLDivElement;
    let editor: monaco.editor.IStandaloneCodeEditor;
    let Monaco;

    onMount(async () => {
        //http://127.0.0.1:8000/config
        let response : string = '';
        await fetch('http://127.0.0.1:8000/config')
            .then((res) => res.json())
            .then((data) => {
                response = (data);
            });
        Monaco = await import('monaco-editor');
        editor = Monaco.editor.create(divEl, {
            value: response,
            language: 'ini',
            theme: 'vs-dark'
        });

        return () => {
            editor.dispose();
        };
    });
    function upload() {
        //make a post request to the server
        let test_value = editor.getValue();
        let data = new Blob([test_value], {type: 'text/plain'});
        let formData = new FormData();
        formData.append('file', data, 'config.cfg');
        fetch('http://127.0.0.1:8000/upload', {method: 'POST', body: formData})
            .then((res) => res.json())
            .then((data) => {
                console.log(data);
            });
    }
    
</script>




<div bind:this={divEl} class="h-screen" style="min-height: 300px;" />
<button type="button" class="btn btn-primary" on:click={() => upload()}>Save j <i class="bi bi-upload"></i></button>
