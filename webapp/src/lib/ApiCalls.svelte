<script lang="ts">
    let lines : any = [];
    function addLine(num : number) {
        for (let i = 0; i < num; i++) {
            lines.push(i + " \n");
        }
    }
    addLine(100000);
    

</script>

<div class="card" style="width: 18rem;">
    <div class="card-body">
      <h5 class="card-title">Api Calls <i class="bi bi-telephone"></i></h5>
      
      <div class="overflow-auto">
        <p class="card-text overflow-auto">{lines}</p>
      </div>
    </div>
  </div>

<style lang="scss">
    .overflow-auto {
        max-height: 300px;
        overflow: auto;
        text-size-adjust: 100%;
    }
    .overflow-auto::-webkit-scrollbar {
        width: 0.5rem;
    }
    .overflow-auto::-webkit-scrollbar-track {
        background: #f1f1f1;
    }
    .overflow-auto::-webkit-scrollbar-thumb {
        background: #888;
    }
</style>