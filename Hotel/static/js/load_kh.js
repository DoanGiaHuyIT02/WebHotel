dskh = [];

function danhSachKhachHang() {

    ten = document.getElementById('name')
    sdt = document.getElementById('phone')
    CCCD = document.getElementById('CCCD')
    diaChi = document.getElementById('address')
    loaiKhach = document.getElementById('select-LoaiKhach')
    table = document.getElementById('table')

    if (ten.value != '' && sdt.value != '' && CCCD.value != '' && diaChi.value != '' && loaiKhach.value != '')
    {
        dskh.push({
            "name": ten.value,
            "phone": sdt.value,
            "CCCD": CCCD.value,
            "address": diaChi.value,
            "loaiKhach": loaiKhach.value
        })

    }
    ten.value=''
    sdt.value=''
    CCCD.value=''
    diaChi.value=''
    table.innerHTML = ''
    for (let i = 0; i < dskh.length; i++){
        table.innerHTML += `<tr>
                        <td>${ i+1 }</td>
                        <td>${dskh[i].name}</td>
                        <td>${dskh[i].phone}</td>
                        <td>${dskh[i].CCCD}</td>
                        <td>${dskh[i].address}</td>
                        <td>${dskh[i].loaiKhach}</td>
                    </tr>`
    }

}


