dsphong = [];

function danhSachPhong() {
    tongTienPhong = 0
    tongTien = 0
    loaiPhong = document.getElementById('select-loaiPhong')
    soLuongPhong = document.getElementById('soLuongPhong')
    donGia = document.getElementById('price')
    table1 = document.getElementById('table1')
    total = document.getElementById('total')



    if (loaiPhong.value != '' && soLuongPhong.value != 0)
    {
        gia = parseInt(donGia.innerHTML.replaceAll(',','').slice(1))

        tongTienPhong = soLuongPhong.value * gia

        const formatter = new Intl.NumberFormat('en-VN', {
            currency: 'VND',
            style: 'currency',
        });

        format = formatter.format(tongTienPhong)

        dsphong.push({
            "tenPhong": loaiPhong.options[loaiPhong.selectedIndex].text,
            "soLuongPhong": soLuongPhong.value,
            "tongTienPhong": format
        })

    }

    table1.innerHTML = ''
    for (let i = 0; i < dsphong.length; i++){
        table1.innerHTML += `<tr>
                        <td>${ i+1 }</td>
                        <td>${dsphong[i].tenPhong}</td>
                        <td>${dsphong[i].soLuongPhong}</td>
                        <td>${dsphong[i].tongTienPhong}</td>
                        <td><button class="btn btn-danger" type="button" onclick="deleteRow(this)">X</button></td>
                    </tr>`
        tongTien += parseInt(dsphong[i].tongTienPhong.replaceAll(',', '').slice(1))
    }

    tongTienThanhToan = tongTien.toLocaleString('vi', {style : 'currency', currency : 'VND'})
    let alertTotal = document.getElementById('alertTotal')
    alertTotal.innerHTML=""
    alertTotal.innerHTML = `<h3>
                        Tổng tiền:
                            <span id="total">${tongTienThanhToan}</span>
                    </h3>
                        `
}

function update_thanhToan() {
    const formatter = new Intl.NumberFormat('en-VN', {
        currency: 'VND',
        style: 'currency',
    });
    loaiPhong = document.getElementById('select-loaiPhong')
    price = document.getElementById('priceRoom')


    if (loaiPhong.value == 1) {
         lp = 3000000
    } else if (loaiPhong.value == 2) {
        lp = 4000000
    } else {
        lp = 5000000
    }
    format = formatter.format(lp)

    price.innerHTML = ''
    price.innerHTML += `<h3>Đơn giá: <span id="price">${format}</span></h3>
    `

}

function deleteRow(r) {
  var i = r.parentNode.parentNode.parentNode.rowIndex;
  if (confirm("Bạn có chắc muốn xóa!") == true)
    document.getElementById("table1").deleteRow(i-1);
}