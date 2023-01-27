<script lang="ts">
    import type monaco from 'monaco-editor';
    import { onMount } from 'svelte';
    let divEl: HTMLDivElement;
    let editor: monaco.editor.IStandaloneCodeEditor;
    let Monaco;
    let files : string[] = [];
    onMount(async () => {
        //http://127.0.0.1:8000/config
        let response : string = '';
        await fetch('http://127.0.0.1:8000/config_list')
            .then((res) => res.json())
            .then((data) => {
                files = (data);
            });
        Monaco = await import('monaco-editor');
        editor = Monaco.editor.create(divEl, {
            value: "no file selected",
            language: 'ini',
            theme: 'vs-dark'
        });
        return () => {
            editor.dispose();
        };
    });
    const reader = new FileReader();

    async function edit(file: string) {
        let response : string = '';
        await fetch('http://127.0.0.1:8000/config/' + file)
            .then((res) => res.json())
            .then((data) => {
                response = (data);
            });
        editor.setValue(response);
    }
    function upload() {
        //make a post request to the server
        let test_value = editor.getValue();
        let data = new Blob([test_value], {type: 'text/plain'});
        let formData = new FormData();
        formData.append('file', data, 'config.cfg');
        fetch('http://127.0.0.1:8000/upload_config', {method: 'POST', body: formData})
            .then((res) => res.json())
            .then((data) => {
                console.log(data);
            });
    }
</script>



<div class="container">
    <div class="row">
      <div class="col-1">
        <ul class="list-group">
            {#each files as file}
                <!-- svelte-ignore missing-declaration -->
                <!-- svelte-ignore a11y-click-events-have-key-events -->
                <li class="list-group-item" on:click={() => edit(file)}>{file}<i class="bi bi-file-earmark"></i></li>
            {/each}
        </ul>        
      </div>
      <div class="col-10">
        <div bind:this={divEl} class="h-screen" style="min-height: 600px;" />
      </div>
      <div class="col-1">
        <button type="button" class="btn btn-primary" on:click={() => upload()}>Save File <i class="bi bi-upload"></i></button>
      </div>
    </div>
  </div>




<style>
    .list-group-item {
        cursor: pointer;
    }
</style>

