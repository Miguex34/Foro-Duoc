$(document).ready(() => {
    $('#respabfecha')[0].valueAsDate = new Date();
    let thead = `
        <th class="theadtitle">Disponibilidad de pabellón</th>
    `;
    let tbody = [];
    for(let block of [...Array(24).keys()].map(x => x+1)) {
        if(block<= 9) {
            thead += `
                <th class="theadhora">${'0' + (block-1) + ':00'} - ${'0' + block + ':00'}</th>
            `;
        } else if(block == 10) {
            thead += `
                <th class="theadhora">${'0' + (block-1) + ':00'} - ${block + ':00'}</th>
            `;
        } else {
            thead += `
                <th class="theadhora">${(block-1) + ':00'} - ${block + ':00'}</th>
            `;
        }

        for(let pabellon of [...Array(4).keys()].map(x => x+1)) {
            if(block == 1) {
                tbody.push('<tr><td class="p-2 tbodytitle">Pabellón ' + pabellon + '</td>');
                tbody[pabellon-1] += '<td class="p-2 tbodyhora"><div class="horablock" id="pab' + (pabellon) + (block-1) + '" pabellon="'+(pabellon)+'" block="'+(block-1)+'">&nbsp;</div></td>';
            } else if(block == 24) {
                tbody[pabellon-1] += '<td class="p-2 tbodyhora"><div class="horablock" id="pab' + (pabellon) + (block-1) + '" pabellon="'+(pabellon)+'" block="'+(block-1)+'">&nbsp;</div></td>';
                tbody[pabellon-1] += '</tr>';
            } else {
                tbody[pabellon-1] += '<td class="p-2 tbodyhora"><div class="horablock" id="pab' + (pabellon) + (block-1) + '" pabellon="'+(pabellon)+'" block="'+(block-1)+'">&nbsp;</div></td>';
            }
        }
    }
    let tablebody = '';
    for(let i of tbody) {
        tablebody += i;
    }
    $('#tablerespabhead').html(thead);
    $('#tablerespabbody').html(tablebody);
});

function oneback() {
    var elem = $('#respabfecha');
    var date = new Date(`${elem[0].value}T00:00`);
    date.setDate(date.getDate()-1)
    elem[0].valueAsDate = date;
}

function oneforward() {
    var elem = $('#respabfecha');
    var date = new Date(`${elem[0].value}T00:00`);
    date.setDate(date.getDate()+1)
    elem[0].valueAsDate = date;
}