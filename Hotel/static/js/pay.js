
ListRoomCus = [];

function addRooms() {
    select_loaiPhong = document.getElementById('select_loaiPhong')
    soLuongKhach = document.getElementById('soLuongKhach')
    ngayNhanPhong = document.getElementById('ngayNhanPhong')
    ngayTraPhong = document.getElementById('ngayTraPhong')
    table = document.getElementById('table')
    btn_XacNhanPhong = document.getElementById('btn_XacNhanPhong')

    if (select_loaiPhong.value == 1) {
        lp = 3500000
    } else if (select_loaiPhong.value == 2) {
        lp = 4000000
    } else {
        lp = 5000000
    }

    priceRoom = lp.toLocaleString('vi', {style : 'currency', currency : 'VND'})


    if (select_loaiPhong.value != '' && ngayNhanPhong.value != '' && ngayTraPhong.value != '') {

        ListRoomCus.push({
            "select_loaiPhong": select_loaiPhong.options[select_loaiPhong.selectedIndex].text,
            "select_loaiPhong_id": select_loaiPhong.value,
            "ngayNhanPhong": ngayNhanPhong.value,
            "ngayTraPhong": ngayTraPhong.value,
            "priceRoom": priceRoom
        })
        btn_XacNhanPhong.style.display = 'none';
    } else if (ngayNhanPhong.value == '' || ngayTraPhong.value == '' ){
        btn_XacNhanPhong.style.display = 'block';
    }

    table.innerHTML = ''
    for (let i = 0; i < ListRoomCus.length; i++){
        table.innerHTML += `<tr>
                        <td>${ i+1 }</td>
                        <td>${ListRoomCus[i].select_loaiPhong}</td>
                        <div style="visibility: hidden;"><input class="text-center" style="border: none; background-color: #fff" value="${ListRoomCus[i].select_loaiPhong_id}" name="loaiPhong_id"/></div>
                        <td>${ListRoomCus[i].priceRoom}</td>
                        <td><input readonly class="text-center" style="border: none; background-color: #fff; outline: none" value="${ListRoomCus[i].ngayNhanPhong}" name="ngayNhan"/></td>
                        <td><input readonly class="text-center" style="border: none; background-color: #fff; outline: none" value="${ListRoomCus[i].ngayTraPhong}" name="ngayTra"/></td>
                        <td><button class="btn btn-danger" type="button" onclick="deleteRow1(this)">X</button></td>
                    </tr>`
    }



}

ListAddCus = [];

function addCus() {
    name1 = document.getElementById('name1')
    CCCD = document.getElementById('CCCD')
    address = document.getElementById('address')
    select_LoaiKhach = document.getElementById('select_LoaiKhach')
    btn_AddCus = document.getElementById('btn_AddCus')
    soluong = document.getElementById('soluong')
    ngayNhanPhong = document.getElementById('ngayNhanPhong')
    ngayTraPhong = document.getElementById('ngayTraPhong')
    tongTien = document.getElementById('tongTien')


    table1 = document.getElementById('table1')
    table2 = document.getElementById('table2')

//Hàm tính toán ngày
    const ngayBD = new Date(ngayNhanPhong.value)
    const ngayKT = new Date(ngayTraPhong.value)

    const oneDay = 1000 * 60 * 60 * 24;

    const so = ngayKT.getTime() - ngayBD.getTime()
    const soNgay = Math.round(so / oneDay)
//Kết thúc tính ngày


   if (select_loaiPhong.value == 1) {
      if (select_LoaiKhach.value == 2) {
        if (soluong.value == 3) {
            lp = (3500000*0.25 + 3500000) * 1.5 * soNgay
        } else {
            lp = 3000000 * 1.5 * soNgay
        }
      } else {
        if (soluong.value == 3) {
            lp = 3500000*0.25 + 3500000 * soNgay
        } else {
            lp = 3500000 * soNgay
        }
      }
    } else if (select_loaiPhong.value == 2) {
        if (select_LoaiKhach.value == 2) {
            if (soluong.value == 3) {
                lp = (4000000 * 0.25 + 4000000) * 1.5 * soNgay
            } else {
                 lp = 4000000 * 1.5 * soNgay
            }
        } else {
            if (soluong.value == 3) {
                lp = 4000000 * 0.25 + 4000000 * soNgay
            } else {
                 lp = 4000000 * soNgay
            }
        }
    } else {
        if (select_LoaiKhach.value == 2) {
             if (soluong.value == 3) {
                lp = (5000000*0.25 + 5000000) * 1.5
            } else {
                 lp = 5000000 * 1.5
            }
        } else {
            if (soluong.value == 3) {
                lp = 5000000*0.25 + 5000000
            } else {
                 lp = 5000000
            }
        }

    }

    priceRoom = lp.toLocaleString('vi', {style : 'currency', currency : 'VND'})



    if (name1.value != '' && CCCD.value != '' && address.value != '' && select_LoaiKhach.value != '') {
        ListAddCus.push({
            "name1": name1.value,
            "CCCD": CCCD.value,
            "address": address.value,
            "select_LoaiKhach": select_LoaiKhach.options[select_LoaiKhach.selectedIndex].text,
            "select_LoaiKhach_id": select_LoaiKhach.value,
            "ngayNhanPhong": ngayNhanPhong.value,
            "ngayTraPhong": ngayTraPhong.value,
            "priceRoom": priceRoom
        })
    }

    name1.value=''
    CCCD.value=''
    address.value=''
    table1.innerHTML = ''
    for (let i = 0; i < ListAddCus.length; i++){
        table1.innerHTML += `<tr>
                        <td>${ i+1 }</td>
                        <td ><input readonly class="text-center" style="border: none; background-color: #fff; outline: none" value="${ListAddCus[i].name1}" name="name"/></td>
                        <td ><input readonly class="text-center" style="border: none; background-color: #fff; outline: none" value="${ListAddCus[i].CCCD}" name="CCCD"/></td>
                        <td ><input readonly class="text-center" style="border: none; background-color: #fff; outline: none" value="${ListAddCus[i].address}" name="address"/></td>
                        <td ><input readonly class="text-center" style="border: none; background-color: #fff; outline: none" value="${ListAddCus[i].select_LoaiKhach}"/></td>
                        <div style="visibility: hidden;"><input value="${ListAddCus[i].select_LoaiKhach_id}" name="loaiKhach"/></div>
                        <td><button class="btn btn-danger" type="button" onclick="deleteRow2(this)">X</button></td>
                    </tr>`
    }

    tongTien.innerHTML = ''
    tongTien.innerHTML += `<h3>Tổng tiền: <span class="cart-amount"><input readonly class="text-center" style="border: none; background-color: #cff4fc; outline: none" name="tongTienKhachHang" value="${priceRoom}"/></span> VNĐ
                        </h3>`

    if (soluong.value == ListAddCus.length) {
        btn_AddCus.setAttribute('disabled', '');
    }


}





function deleteRow1(r) {
  var i = r.parentNode.parentNode.parentNode.rowIndex;
  if (confirm("Bạn có chắc muốn xóa!") == true) {
        document.getElementById("table").deleteRow(i-1);
        document.getElementById("table1").deleteRow(i-1);
  }
}

function deleteRow2(r) {
  var i = r.parentNode.parentNode.parentNode.rowIndex;
  if (confirm("Bạn có chắc muốn xóa!") == true) {
        document.getElementById("table1").deleteRow(i-1);
  }
}

function thongBaoXacNhan() {
    alert('Bạn đã chắc chắn đặt phòng !!!!')
}

