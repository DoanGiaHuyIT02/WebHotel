ListAddCusEmp = [];

function addCusEmp() {
    e_name = document.getElementById('e_name')
    e_CCCD = document.getElementById('e_CCCD')
    e_address = document.getElementById('e_address')
    e_select_LoaiKhach = document.getElementById('e_select_LoaiKhach')

    e_ngayNhanPhong = document.getElementById('e_ngayNhanPhong')
    e_ngayTraPhong = document.getElementById('e_ngayTraPhong')
    e_soPhong = document.getElementById('e_soPhong')
    e_select_loaiPhong = document.getElementById('e_select_loaiPhong')

    addCus = document.getElementById('addCus')
    e_tongTien = document.getElementById('e_tongTien')
    timeBook = document.getElementById('timeBook')
    e_table = document.getElementById('e_table')

//Hàm tính toán ngày
    const ngayBD = new Date(e_ngayNhanPhong.value)
    const ngayKT = new Date(e_ngayTraPhong.value)

    const oneDay = 1000 * 60 * 60 * 24;

    const so = ngayKT.getTime() - ngayBD.getTime()
    const soNgay = Math.round(so / oneDay)
//Kết thúc tính ngày


   if (e_select_loaiPhong.value == 1) {
      if (e_select_LoaiKhach.value == 2) {
        if (ListAddCusEmp.length == 3) {
            lp = (3500000*0.25 + 3500000) * 1.5 * soNgay
        } else {
            lp = 3500000 * 1.5 * soNgay
        }
      } else {
        if (ListAddCusEmp.length == 3) {
            lp = 3500000*0.25 + 3500000 * soNgay
        } else {
            lp = 3500000 * soNgay
        }
      }
    } else if (e_select_loaiPhong.value == 2) {
        if (e_select_LoaiKhach.value == 2) {
            if (ListAddCusEmp.length == 3) {
                lp = (4000000 * 0.25 + 4000000) * 1.5 * soNgay
            } else {
                 lp = 4000000 * 1.5 * soNgay
            }
        } else {
            if (ListAddCusEmp.length == 3) {
                lp = 4000000 * 0.25 + 4000000 * soNgay
            } else {
                 lp = 4000000 * soNgay
            }
        }
    } else {
        if (e_select_loaiPhong.value == 2) {
             if (ListAddCusEmp.length == 3) {
                lp = (5000000*0.25 + 5000000) * 1.5
            } else {
                 lp = 5000000 * 1.5
            }
        } else {
            if (ListAddCusEmp.length == 3) {
                lp = 5000000*0.25 + 5000000
            } else {
                 lp = 5000000
            }
        }

    }

    priceRoom = lp.toLocaleString('vi', {style : 'currency', currency : 'VND'})


    if (e_ngayNhanPhong.value == '' && e_ngayTraPhong.value == '') {
        alert("Vui lòng nhập ngày tháng")
    } else if (e_name.value != '' && e_CCCD.value != '' && e_address.value != '' && e_select_LoaiKhach.value != '') {
            ListAddCusEmp.push({
                "e_name": e_name.value,
                "e_CCCD": e_CCCD.value,
                "e_address": e_address.value,
                "e_select_LoaiKhach": e_select_LoaiKhach.options[e_select_LoaiKhach.selectedIndex].text,
                "select_LoaiKhach_id": e_select_LoaiKhach.value,
                "e_ngayNhanPhong": e_ngayNhanPhong.value,
                "e_ngayTraPhong": e_ngayTraPhong.value,
                "priceRoom": priceRoom
            })
        }

    e_name.value=''
    e_CCCD.value=''
    e_address.value=''
    e_table.innerHTML = ''
    for (let i = 0; i < ListAddCusEmp.length; i++){
        e_table.innerHTML += `<tr>
                        <td>${ i+1 }</td>
                        <td ><input class="text-center" style="border: none; background-color: #fff" value="${ListAddCusEmp[i].e_name}" name="name" /></td>
                        <td ><input class="text-center" style="border: none; background-color: #fff" value="${ListAddCusEmp[i].e_CCCD}" name="CCCD" /></td>
                        <td ><input class="text-center" style="border: none; background-color: #fff" value="${ListAddCusEmp[i].e_address}" name="address" /></td>
                        <td ><input class="text-center" style="border: none; background-color: #fff" value="${ListAddCusEmp[i].e_select_LoaiKhach}" name="e_select_LoaiKhach" disabled/></td>
                        <div style="visibility: hidden;"><input value="${ListAddCusEmp[i].select_LoaiKhach_id}" name="select_LoaiKhach_id"/></div>
                        <div style="display: none"><input value="${priceRoom}" name="priceRoom"/></div>
                        <td><button class="btn btn-danger" type="button" onclick="deleteRow3(this)">X</button></td>
                    </tr>`
    }

    e_tongTien.innerHTML = ''
    e_tongTien.innerHTML += `<h3>Tổng tiền:
                                <span class="cart-amount">
                                    <input style="border: none; background-color: #cff4fc" disabled name="e_tongTien" value="${priceRoom}"/>
                                </span> VNĐ
                            </h3>`

    if (ListAddCusEmp.length > 2) {
        addCus.setAttribute('disabled', '');
    }
}


ListTime = [];

function datPhong() {

    e_ngayNhanPhong = document.getElementById('e_ngayNhanPhong')
    e_ngayTraPhong = document.getElementById('e_ngayTraPhong')
    e_soPhong = document.getElementById('e_soPhong')
    e_select_loaiPhong = document.getElementById('e_select_loaiPhong')
    e_name_check_in = document.getElementById('e_name_check_in')
    e_phone_check_in = document.getElementById('e_phone_check_in')
    e_CCCD_check_in = document.getElementById('e_CCCD_check_in')
    e_address_check_in = document.getElementById('e_address_check_in')


    btn_xacNhanPhong = document.getElementById('btn_xacNhanPhong')
    timeBook = document.getElementById('timeBook')
    timeBook2 = document.getElementById('timeBook2')
    timeBook3 = document.getElementById('timeBook3')

    if (e_ngayNhanPhong.value != '' && e_ngayTraPhong.value != '' && e_soPhong.value != '' && e_select_loaiPhong.value != '') {
        ListTime.push({
            "e_select_loaiPhong": e_select_loaiPhong.options[e_select_LoaiKhach.selectedIndex].text,
            "e_select_loaiPhong_id": e_select_loaiPhong.value,
            "e_soPhong": e_soPhong.options[e_soPhong.selectedIndex].text,
            "e_ngayNhanPhong": e_ngayNhanPhong.value,
            "e_ngayTraPhong": e_ngayTraPhong.value,
            "e_name_check_in": e_name_check_in.value,
            "e_phone_check_in": e_phone_check_in.value,
            "e_CCCD_check_in": e_CCCD_check_in.value,
            "e_address_check_in": e_address_check_in.value
        })
    }
    timeBook3.innerHTML = ''
    for (let i = 0; i < ListTime.length; i++){
        timeBook3.innerHTML += `
                             <td colspan="5">Người đặt phòng:
                                <input style="border: none; background-color: #fff" value="${ListTime[i].e_name_check_in}" name="e_name_check_in"/>
                             </td>
                            <div style="display: none"><input value="${ListTime[i].e_phone_check_in}" name="e_phone_check_in"/></div>
                            <div style="display: none"><input value="${ListTime[i].e_CCCD_check_in}" name="e_CCCD_check_in"/></div>
                            <div style="display: none"><input value="${ListTime[i].e_address_check_in}" name="e_address_check_in"/></div>
                                `
    }
    timeBook.innerHTML = ''
    for (let i = 0; i < ListTime.length; i++){
        timeBook.innerHTML += `
                             <td colspan="3">Ngày nhận phòng:
                                <input style="border: none; background-color: #fff" value="${ListTime[i].e_ngayNhanPhong}" name="e_ngayNhanPhong"/>
                             </td>
                            <td colspan="2">Ngày trả phòng:
                                <input style="border: none; background-color: #fff" value="${ListTime[i].e_ngayTraPhong}" name="e_ngayTraPhong"/>
                            </td>
                                `
    }
    timeBook2.innerHTML = ''
    for (let i = 0; i < ListTime.length; i++){
        timeBook2.innerHTML += `
                             <td colspan="3">Loại phòng:
                                <input style="border: none; background-color: #fff" value="${ListTime[i].e_select_loaiPhong}" name="e_select_loaiPhong"/>
                             </td>
                             <div style="display: none"><input value="${ListTime[i].e_select_loaiPhong_id}" name="e_select_loaiPhong_id"/></div>
                            <td colspan="2">Số phòng:
                                <input style="border: none; background-color: #fff" value="${ListTime[i].e_soPhong}" name="e_soPhong"/>
                            </td>
                                `
    }


    btn_xacNhanPhong.style.display = 'none';

}

function deleteRow3(r) {
  var i = r.parentNode.parentNode.parentNode.rowIndex;
  if (confirm("Bạn có chắc muốn xóa!") == true) {
        document.getElementById("e_table").deleteRow(i-1);
  }
}

function thongBaoXacNhan1() {
    alert('Bạn đã chắc chắn đặt phòng !!!!')
}

function show_so_phong(loaiPhong_id) {
    fetch('/api/book/' + loaiPhong_id.value, {
      method: "GET",
      dataType: 'json',
      ContentType: 'application/json'
    }).then(res => res.json()).then(data => {
        const soPhongArray = data.soPhongArr; // ['1','2','3']
        console.log(soPhongArray.value)

        var select = document.getElementById('e_soPhong');
        select.innerHTML = "";

        for (var i = 0; i<=soPhongArray.length - 1; i++){
            var opt = document.createElement('option');
            opt.value = soPhongArray[i];
            opt.innerHTML = soPhongArray[i];
            select.appendChild(opt);
        }


    }).catch((err) => {
      console.log(err)
    })
}





