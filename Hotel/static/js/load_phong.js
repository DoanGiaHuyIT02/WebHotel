dsphong = [];

function danhSachPhong() {
    loaiPhong = document.getElementById('select-loaiPhong')
    soLuongPhong = document.getElementById('soLuongPhong')
    table1 = document.getElementById('table1')


    if (loaiPhong.value != '' && soLuongPhong.value != 0)
    {
        dsphong.push({
            "loaiPhong": loaiPhong.value,
            "soLuongPhong": soLuongPhong.value

        })

    }

    table1.innerHTML = ''
    for (let i = 0; i < dsphong.length; i++){
        table1.innerHTML += `<tr>
                        <td>${ i+1 }</td>
                        <td>${dsphong[i].loaiPhong}</td>
                        <td>${dsphong[i].soLuongPhong}</td>
                    </tr>`
    }

}