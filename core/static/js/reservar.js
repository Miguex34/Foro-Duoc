var selectedblocks = {};
var todaydate = new Date();
var general = 0;

$(document).ready(() => {
    $('#respabfecha')[0].valueAsDate = new Date();
    todaydate = $('#respabfecha')[0].value;
    
    setTable();

    $('.horablock').click(elem => reshora(elem));
});

$('#respabfecha').change(() => {
    setTable();
    todaydate = $('#respabfecha')[0].value;
    $('.horablock').click(elem => reshora(elem));
    [...$('.getinput')].forEach(htmlElem => {
        let date = htmlElem.children[0].value;
        let pab = htmlElem.children[1].value;
        let block = htmlElem.children[2].value;
        try {
            if(date == todaydate) {
                $('#pab' + pab + '' + block)[0].classList.add('selected');
            }
        } catch (error) {
            console.log(error);
        }
    });
});

function deleteselected(elem) {
    var vpab = elem.getAttribute('pab');
    var vblock = elem.getAttribute('block');
    var vdate = elem.getAttribute('date');
    selectedblocks[vdate] = selectedblocks[vdate].filter(e => e != vblock);
    $('#' + vdate + vpab + vblock)[0].outerHTML = '';
    if(vdate == todaydate) {
        $('#pab' + vpab + '' + vblock)[0].classList.remove('selected');
    }
}

function oneback() {
    var elem = $('#respabfecha');
    var date = new Date(`${$('#respabfecha')[0].value}T00:00`);
    date.setDate(date.getDate()-1)
    elem[0].valueAsDate = date;
    elem.trigger('change');
}

function oneforward() {
    var elem = $('#respabfecha');
    var date = new Date(`${$('#respabfecha')[0].value}T00:00`);
    date.setDate(date.getDate()+1)
    elem[0].valueAsDate = date;
    elem.trigger('change');
}

function reshora(elem) {
    var target = elem.target;
    var lista = $('#listareservar');
    var pab = Number.parseInt(elem.target.getAttribute('pabellon'));
    var block = Number.parseInt(elem.target.getAttribute('block'));
    var date = $('#respabfecha').val();
    if (![...target.classList].includes('selected')) {
        var htmladd = '';
        var includeblock;
        try {
            includeblock = !selectedblocks[$('#respabfecha')[0].value].includes(block);
        } catch(error) {
            selectedblocks[$('#respabfecha')[0].value] = [];
            includeblock = true;
        }
        if(includeblock) {
            target.classList.add('selected');
            selectedblocks[$('#respabfecha')[0].value].push(block);
            general += 1;
            if(block <= 8) {
                htmladd = `
                <div id="${todaydate + '' + pab + '' + block}" class="getinput">
                    <input type="hidden" value="${date}">
                    <input type="hidden" value="${pab}">
                    <input type="hidden" value="${block}">
                    <p class="pt-2 pb-2 d-inline-block pt-4">
                        <span class="fw-bold">Pabellón - ${pab}:</span>
                        <span class="fst-italic fw-light">0${block}:00 - 0${block+1}:00, ${date}</span></span>
                    </p>
                    <button class="icontrash d-inline-block ms-3 ${pab + '' + block}"
                        onclick="deleteselected(this);" pab="${pab}" block="${block}" date="${todaydate}">
                        <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-trash" 
                            width="20" height="20" viewBox="0 0 24 24" stroke-width="1" stroke="#000000" 
                            fill="none" stroke-linecap="round" stroke-linejoin="round">
                        <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
                        <line x1="4" y1="7" x2="20" y2="7" />
                        <line x1="10" y1="11" x2="10" y2="17" />
                        <line x1="14" y1="11" x2="14" y2="17" />
                        <path d="M5 7l1 12a2 2 0 0 0 2 2h8a2 2 0 0 0 2 -2l1 -12" />
                        <path d="M9 7v-3a1 1 0 0 1 1 -1h4a1 1 0 0 1 1 1v3" />
                    </svg>
                    </button>
                    <br>
                </div>
                `;
            } else if(block == 9) {
                htmladd = `
                <div id="${pab + '' + block}">
                <p class="pt-2 pb-2 d-inline-block pt-4">
                    <span class="fw-bold">Pabellón - ${pab}:</span>
                    <span class="fst-italic fw-light">0${block}:00 - ${block+1}:00, ${date}</span>
                </p>
                <button class="icontrash d-inline-block ms-3 ${pab + '' + block}" onclick="deleteselected(this);">
                    <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-trash" 
                        width="20" height="20" viewBox="0 0 24 24" stroke-width="1" stroke="#000000" 
                        fill="none" stroke-linecap="round" stroke-linejoin="round">
                    <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
                    <line x1="4" y1="7" x2="20" y2="7" />
                    <line x1="10" y1="11" x2="10" y2="17" />
                    <line x1="14" y1="11" x2="14" y2="17" />
                    <path d="M5 7l1 12a2 2 0 0 0 2 2h8a2 2 0 0 0 2 -2l1 -12" />
                    <path d="M9 7v-3a1 1 0 0 1 1 -1h4a1 1 0 0 1 1 1v3" />
                </svg>
                </button>
                <br>
                </div>
                `;
            } else {
                htmladd = `
                <div id="${pab + '' + block}">
                <p class="pt-2 pb-2 d-inline-block pt-4">
                    <span class="fw-bold">Pabellón - ${pab}:</span>
                    <span class="fst-italic fw-light">${block}:00 - ${block+1}:00, ${date}</span>
                </p>
                <button class="icontrash d-inline-block ms-3 ${pab + '' + block }" onclick="deleteselected(this);">
                    <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-trash" 
                        width="20" height="20" viewBox="0 0 24 24" stroke-width="1" stroke="#000000" 
                        fill="none" stroke-linecap="round" stroke-linejoin="round">
                    <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
                    <line x1="4" y1="7" x2="20" y2="7" />
                    <line x1="10" y1="11" x2="10" y2="17" />
                    <line x1="14" y1="11" x2="14" y2="17" />
                    <path d="M5 7l1 12a2 2 0 0 0 2 2h8a2 2 0 0 0 2 -2l1 -12" />
                    <path d="M9 7v-3a1 1 0 0 1 1 -1h4a1 1 0 0 1 1 1v3" />
                </svg>
                </button>
                <br>
                </div>
                `;
            }
            lista.html(lista.html() + htmladd);
        } else {
            Swal.fire({
                title: '<strong>Error</strong>',
                icon: 'error',
                html: '<p>No se puede seleccionar 2 bloques simultaneos.</p>',
                showCloseButton: true,
                confirmButtonText: 'Aceptar'
            });
        }
    } else {
        deleteselected($('.' + pab + '' + block+ '[date="'+todaydate+'"]')[0]);
    }
}

function setTable() {
    let thead = `
        <th class="theadtitle">Reserva de pabellón</th>
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
}

function gotorecursos() {
    location.href = '/programacion/recursos/disponibilidad/';
}