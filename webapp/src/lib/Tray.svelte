<script lang="ts">
    // export let safeMove = (x: number, y: number, z: number) => {};
    // export let addCommandToQueue = (cell: string) => {};
    // let a0x: number = 0;
    // let a0y: number = 0;
    // let a0z: number = 0;
    // let trayOffsetX: number = 0;
    // let trayOffsetY: number = 0;
    // let probingOffset: number = 0;
    // import { config } from "../stores/machine_config.js";
    // config.subscribe((config) => {
    //   a0x = config.trayA0.x;
    //   a0y = config.trayA0.y;
    //   a0z = config.trayA0.z;
    //   trayOffsetX = config.trayOffset.x;
    //   trayOffsetY = config.trayOffset.y;
    //   probingOffset = config.probe.probingOffset;
    // });
  
    // function generateCellCoordinates(letter: string, number: number) {
    //   let x = a0x + (letter.charCodeAt(0) - 65) * trayOffsetX;
    //   let y = a0y + number * trayOffsetY;
    //   let z = a0z;
    //   return [x, y, z];
    // }
    let generatedX: number = 0;
    let generatedY: number = 0;
    let generatedZ: number = 0;
    let generatedCell: string = "";
  
    // function sendToCell(cell: string) {
    //   const letter = cell.charAt(0);
    //   const number = parseInt(cell.charAt(1));
    //   let coordinates = generateCellCoordinates(letter, number);
    //   safeMove(coordinates[0], coordinates[1], coordinates[2]);
    //   //for testing
    //   generatedX = coordinates[0];
    //   generatedY = coordinates[1];
    //   generatedZ = coordinates[2];
    //   generatedCell = cell;
    // }
    // //tray leveing code
    // let textInput: string = "";
    let position: { x: number; y: number; z: number } = { x: 0, y: 0, z: 0 };
    // async function probeCell(cell: string) {
    //   let coordinates = generateCellCoordinates(
    //     cell.charAt(0),
    //     parseInt(cell.charAt(1))
    //   );
    //   safeMove(coordinates[0], coordinates[1], coordinates[2] + probingOffset);
    //   addCommandToQueue("G30");
    //   //wait for 5 seconds
    //   await new Promise((resolve) => setTimeout(resolve, 5000));
    // }
    // export function parse(x: string, y: string, z: string) {
    //   position.x = parseFloat(x);
    //   position.y = parseFloat(y);
    //   position.z = parseFloat(z);
    //   //update store
    //   config.update((config) => {
    //     console.log("updating config");
    //     config.spawnCubeConfig.x = position.x;
    //     config.spawnCubeConfig.y = position.y;
    //     config.spawnCubeConfig.z = position.z;
    //     config.spawnCubeConfig.spawn = true;
    //     return config;
    //   });
    // }
    function sendToCell(cell: string) {
      console.log("sending to cell");
    }
    
  </script>
  <!-- svelte-ignore a11y-click-events-have-key-events -->
  <div class="card bg-dark text-white">
    <div class="card-body">
      <h5 class="card-title">Chip Tray 🥔</h5>
      <p class="card-text">
        <small
          >cell : {generatedCell} x: {generatedX} y: {generatedY} z: {generatedZ}</small
        >
        <small
          >probe : {generatedCell} x: {position.x} y: {position.y} z: {position.z}</small
        >
      </p>
      <div class="container">
        <table
          class="table table-borderless table-dark"
          style="width: 10rem; height: 10rem;"
        >
          <tbody>
            <tr>
              <td on:click={() => sendToCell("H20")}>H20</td>
              <td on:click={() => sendToCell("G20")}>G20</td>
              <td on:click={() => sendToCell("F20")}>F20</td>
              <td on:click={() => sendToCell("E20")}>E20</td>
              <td on:click={() => sendToCell("D20")}>D20</td>
              <td on:click={() => sendToCell("C20")}>C20</td>
              <td on:click={() => sendToCell("B20")}>B20</td>
              <td on:click={() => sendToCell("A20")}>A20</td>
            </tr>
            <tr>
              <td on:click={() => sendToCell("H19")}>H19</td>
              <td on:click={() => sendToCell("G19")}>G19</td>
              <td on:click={() => sendToCell("F19")}>F19</td>
              <td on:click={() => sendToCell("E19")}>E19</td>
              <td on:click={() => sendToCell("D19")}>D19</td>
              <td on:click={() => sendToCell("C19")}>C19</td>
              <td on:click={() => sendToCell("B19")}>B19</td>
              <td on:click={() => sendToCell("A19")}>A19</td>
            </tr>
            <tr>
              <td on:click={() => sendToCell("H18")}>H18</td>
              <td on:click={() => sendToCell("G18")}>G18</td>
              <td on:click={() => sendToCell("F18")}>F18</td>
              <td on:click={() => sendToCell("E18")}>E18</td>
              <td on:click={() => sendToCell("D18")}>D18</td>
              <td on:click={() => sendToCell("C18")}>C18</td>
              <td on:click={() => sendToCell("B18")}>B18</td>
              <td on:click={() => sendToCell("A18")}>A18</td>
            </tr>
            <tr>
              <td on:click={() => sendToCell("H17")}>H17</td>
              <td on:click={() => sendToCell("G17")}>G17</td>
              <td on:click={() => sendToCell("F17")}>F17</td>
              <td on:click={() => sendToCell("E17")}>E17</td>
              <td on:click={() => sendToCell("D17")}>D17</td>
              <td on:click={() => sendToCell("C17")}>C17</td>
              <td on:click={() => sendToCell("B17")}>B17</td>
              <td on:click={() => sendToCell("A17")}>A17</td>
            </tr>
            <tr>
              <td on:click={() => sendToCell("H16")}>H16</td>
              <td on:click={() => sendToCell("G16")}>G16</td>
              <td on:click={() => sendToCell("F16")}>F16</td>
              <td on:click={() => sendToCell("E16")}>E16</td>
              <td on:click={() => sendToCell("D16")}>D16</td>
              <td on:click={() => sendToCell("C16")}>C16</td>
              <td on:click={() => sendToCell("B16")}>B16</td>
              <td on:click={() => sendToCell("A16")}>A16</td>
            </tr>
            <tr>
              <td on:click={() => sendToCell("H15")}>H15</td>
              <td on:click={() => sendToCell("G15")}>G15</td>
              <td on:click={() => sendToCell("F15")}>F15</td>
              <td on:click={() => sendToCell("E15")}>E15</td>
              <td on:click={() => sendToCell("D15")}>D15</td>
              <td on:click={() => sendToCell("C15")}>C15</td>
              <td on:click={() => sendToCell("B15")}>B15</td>
              <td on:click={() => sendToCell("A15")}>A15</td>
            </tr>
            <tr>
              <td on:click={() => sendToCell("H14")}>H14</td>
              <td on:click={() => sendToCell("G14")}>G14</td>
              <td on:click={() => sendToCell("F14")}>F14</td>
              <td on:click={() => sendToCell("E14")}>E14</td>
              <td on:click={() => sendToCell("D14")}>D14</td>
              <td on:click={() => sendToCell("C14")}>C14</td>
              <td on:click={() => sendToCell("B14")}>B14</td>
              <td on:click={() => sendToCell("A14")}>A14</td>
            </tr>
            <tr>
              <td on:click={() => sendToCell("H13")}>H13</td>
              <td on:click={() => sendToCell("G13")}>G13</td>
              <td on:click={() => sendToCell("F13")}>F13</td>
              <td on:click={() => sendToCell("E13")}>E13</td>
              <td on:click={() => sendToCell("D13")}>D13</td>
              <td on:click={() => sendToCell("C13")}>C13</td>
              <td on:click={() => sendToCell("B13")}>B13</td>
              <td on:click={() => sendToCell("A13")}>A13</td>
            </tr>
            <tr>
              <td on:click={() => sendToCell("H12")}>H12</td>
              <td on:click={() => sendToCell("G12")}>G12</td>
              <td on:click={() => sendToCell("F12")}>F12</td>
              <td on:click={() => sendToCell("E12")}>E12</td>
              <td on:click={() => sendToCell("D12")}>D12</td>
              <td on:click={() => sendToCell("C12")}>C12</td>
              <td on:click={() => sendToCell("B12")}>B12</td>
              <td on:click={() => sendToCell("A12")}>A12</td>
            </tr>
            <tr>
              <td on:click={() => sendToCell("H11")}>H11</td>
              <td on:click={() => sendToCell("G11")}>G11</td>
              <td on:click={() => sendToCell("F11")}>F11</td>
              <td on:click={() => sendToCell("E11")}>E11</td>
              <td on:click={() => sendToCell("D11")}>D11</td>
              <td on:click={() => sendToCell("C11")}>C11</td>
              <td on:click={() => sendToCell("B11")}>B11</td>
              <td on:click={() => sendToCell("A11")}>A11</td>
            </tr>
            <tr>
              <td on:click={() => sendToCell("H10")}>H10</td>
              <td on:click={() => sendToCell("G10")}>G10</td>
              <td on:click={() => sendToCell("F10")}>F10</td>
              <td on:click={() => sendToCell("E10")}>E10</td>
              <td on:click={() => sendToCell("D10")}>D10</td>
              <td on:click={() => sendToCell("C10")}>C10</td>
              <td on:click={() => sendToCell("B10")}>B10</td>
              <td on:click={() => sendToCell("A10")}>A10</td>
            </tr>
            <tr>
              <td on:click={() => sendToCell("H9")}>H9</td>
              <td on:click={() => sendToCell("G9")}>G9</td>
              <td on:click={() => sendToCell("F9")}>F9</td>
              <td on:click={() => sendToCell("E9")}>E9</td>
              <td on:click={() => sendToCell("D9")}>D9</td>
              <td on:click={() => sendToCell("C9")}>C9</td>
              <td on:click={() => sendToCell("B9")}>B9</td>
              <td on:click={() => sendToCell("A9")}>A9</td>
            </tr>
            <tr>
              <td on:click={() => sendToCell("H8")}>H8</td>
              <td on:click={() => sendToCell("G8")}>G8</td>
              <td on:click={() => sendToCell("F8")}>F8</td>
              <td on:click={() => sendToCell("E8")}>E8</td>
              <td on:click={() => sendToCell("D8")}>D8</td>
              <td on:click={() => sendToCell("C8")}>C8</td>
              <td on:click={() => sendToCell("B8")}>B8</td>
              <td on:click={() => sendToCell("A8")}>A8</td>
            </tr>
            <tr>
              <td on:click={() => sendToCell("H7")}>H7</td>
              <td on:click={() => sendToCell("G7")}>G7</td>
              <td on:click={() => sendToCell("F7")}>F7</td>
              <td on:click={() => sendToCell("E7")}>E7</td>
              <td on:click={() => sendToCell("D7")}>D7</td>
              <td on:click={() => sendToCell("C7")}>C7</td>
              <td on:click={() => sendToCell("B7")}>B7</td>
              <td on:click={() => sendToCell("A7")}>A7</td>
            </tr>
            <tr>
              <td on:click={() => sendToCell("H6")}>H6</td>
              <td on:click={() => sendToCell("G6")}>G6</td>
              <td on:click={() => sendToCell("F6")}>F6</td>
              <td on:click={() => sendToCell("E6")}>E6</td>
              <td on:click={() => sendToCell("D6")}>D6</td>
              <td on:click={() => sendToCell("C6")}>C6</td>
              <td on:click={() => sendToCell("B6")}>B6</td>
              <td on:click={() => sendToCell("A6")}>A6</td>
            </tr>
            <tr>
              <td on:click={() => sendToCell("H5")}>H5</td>
              <td on:click={() => sendToCell("G5")}>G5</td>
              <td on:click={() => sendToCell("F5")}>F5</td>
              <td on:click={() => sendToCell("E5")}>E5</td>
              <td on:click={() => sendToCell("D5")}>D5</td>
              <td on:click={() => sendToCell("C5")}>C5</td>
              <td on:click={() => sendToCell("B5")}>B5</td>
              <td on:click={() => sendToCell("A5")}>A5</td>
            </tr>
            <tr>
              <td on:click={() => sendToCell("H4")}>H4</td>
              <td on:click={() => sendToCell("G4")}>G4</td>
              <td on:click={() => sendToCell("F4")}>F4</td>
              <td on:click={() => sendToCell("E4")}>E4</td>
              <td on:click={() => sendToCell("D4")}>D4</td>
              <td on:click={() => sendToCell("C4")}>C4</td>
              <td on:click={() => sendToCell("B4")}>B4</td>
              <td on:click={() => sendToCell("A4")}>A4</td>
            </tr>
            <tr>
              <td on:click={() => sendToCell("H3")}>H3</td>
              <td on:click={() => sendToCell("G3")}>G3</td>
              <td on:click={() => sendToCell("F3")}>F3</td>
              <td on:click={() => sendToCell("E3")}>E3</td>
              <td on:click={() => sendToCell("D3")}>D3</td>
              <td on:click={() => sendToCell("C3")}>C3</td>
              <td on:click={() => sendToCell("B3")}>B3</td>
              <td on:click={() => sendToCell("A3")}>A3</td>
            </tr>
            <tr>
              <td on:click={() => sendToCell("H2")}>H2</td>
              <td on:click={() => sendToCell("G2")}>G2</td>
              <td on:click={() => sendToCell("F2")}>F2</td>
              <td on:click={() => sendToCell("E2")}>E2</td>
              <td on:click={() => sendToCell("D2")}>D2</td>
              <td on:click={() => sendToCell("C2")}>C2</td>
              <td on:click={() => sendToCell("B2")}>B2</td>
              <td on:click={() => sendToCell("A2")}>A2</td>
            </tr>
            <tr>
              <td on:click={() => sendToCell("H1")}>H1</td>
              <td on:click={() => sendToCell("G1")}>G1</td>
              <td on:click={() => sendToCell("F1")}>F1</td>
              <td on:click={() => sendToCell("E1")}>E1</td>
              <td on:click={() => sendToCell("D1")}>D1</td>
              <td on:click={() => sendToCell("C1")}>C1</td>
              <td on:click={() => sendToCell("B1")}>B1</td>
              <td on:click={() => sendToCell("A1")}>A1</td>
            </tr>
            <tr>
              <td on:click={() => sendToCell("H0")}>H0</td>
              <td on:click={() => sendToCell("G0")}>G0</td>
              <td on:click={() => sendToCell("F0")}>F0</td>
              <td on:click={() => sendToCell("E0")}>E0</td>
              <td on:click={() => sendToCell("D0")}>D0</td>
              <td on:click={() => sendToCell("C0")}>C0</td>
              <td on:click={() => sendToCell("B0")}>B0</td>
              <td on:click={() => sendToCell("A0")}>A0</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
  
  <style>
    .table {
      cursor: pointer;
      font-size: 0.75vw;
      border-collapse: collapse;
      padding: 0;
      margin: 0;
    }
    .table > :not(caption) > * > * {
      border: 1px solid rgb(99, 99, 99);
      padding: 0.25em 0.5em;
    }
    .container {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      width: 100%;
      height: 100%;
    }
  </style>
  