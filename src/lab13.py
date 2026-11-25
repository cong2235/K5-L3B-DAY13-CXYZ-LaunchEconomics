"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import sys
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    if p == 0:
        return math.inf if k is None else k
    return ti_le_thanh_cong(p, k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if p == 0 or k == 0:
        return 0.0
    if k is None or p == 1:
        return 1.0
    return -math.expm1(k * math.log1p(-p))


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    thanh_cong = ti_le_thanh_cong(p, k)
    if thanh_cong == 0:
        return math.inf
    return so_lan_chay_ky_vong(p, k) / thanh_cong


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
def mo_hinh(runs, reqs, gia_vao=GIA_VAO, gia_ra=GIA_RA, gia_tool=GIA_TOOL, luong_phut=LUONG_PHUT,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Tính chi phí của mọi lần chạy thuộc reqs, kể cả lần lỗi."""
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        reqs = reqs.copy()
        vuot_gioi_han = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot_gioi_han, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot_gioi_han, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token = runs['tokens_in'] * gia_vao / 1000 + runs['tokens_out'] * gia_ra / 1000
    tien_tool = runs['tool_calls'] * gia_tool
    token = tien_token.sum()
    tool = tien_tool.sum()
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = token + tool + xem_lai + lam_lai
    thanh_cong = (reqs['ket_qua'] == 'thanh_cong').sum()
    return {
        'token': token,
        'tool': tool,
        'chay_lai': (tien_token + tien_tool)[runs['attempt'] > 1].sum(),
        'xem_lai': xem_lai,
        'lam_lai': lam_lai,
        'tong': tong,
        'thanh_cong': thanh_cong,
        'cps': tong / thanh_cong if thanh_cong else math.inf,
        'hoa_don_moi_yc': (token + tool) / len(reqs) if len(reqs) else math.nan,
    }


def in_bang_do_nhay(runs, reqs, cps_goc, reqs_pham_vi):
    """In các bảng B1–B4 từ cùng mô hình chi phí của A2."""
    token_gap_doi = {'gia_vao': 2 * GIA_VAO, 'gia_ra': 2 * GIA_RA}
    theo_gioi_han = {lan: mo_hinh(runs, reqs, max_lan_chay=lan) for lan in (1, 2, 3)}
    kich_ban = [
        ('Giá token', 'gấp đôi', mo_hinh(runs, reqs, **token_gap_doi)['cps']),
        ('Giá token', 'giảm một nửa', mo_hinh(runs, reqs, gia_vao=GIA_VAO / 2, gia_ra=GIA_RA / 2)['cps']),
        ('Tỉ lệ xem lại', 'gấp đôi', mo_hinh(runs, reqs, he_so_xem_lai=2)['cps']),
        ('Tỉ lệ xem lại', 'giảm một nửa', mo_hinh(runs, reqs, he_so_xem_lai=0.5)['cps']),
        ('Số ca làm lại', 'gấp đôi', mo_hinh(runs, reqs, he_so_lam_lai=2)['cps']),
        ('Số ca làm lại', 'giảm một nửa', mo_hinh(runs, reqs, he_so_lam_lai=0.5)['cps']),
        ('Lương nhân viên', 'tăng 25%', mo_hinh(runs, reqs, luong_phut=LUONG_PHUT * 1.25)['cps']),
        ('Giới hạn chạy', 'tối đa 2 lần', theo_gioi_han[2]['cps']),
        ('Giới hạn chạy', 'tối đa 1 lần', theo_gioi_han[1]['cps']),
    ]

    print('\nB1 · Đổi từng yếu tố')
    print('Kịch bản | CPS (simulated) | Thay đổi so với A2 (simulated)')
    tac_dong_theo_yeu_to = {}
    for yeu_to, thay_doi, cps in kich_ban:
        tac_dong = cps / cps_goc - 1
        tac_dong_theo_yeu_to[yeu_to] = max(tac_dong_theo_yeu_to.get(yeu_to, 0), abs(tac_dong))
        print(f'{yeu_to} {thay_doi} | {cps:,.0f} đ | {tac_dong:+.1%}')

    print('\nB2 · Đổi một cặp và xếp hạng (simulated)')
    cps_cap = mo_hinh(runs, reqs, **token_gap_doi, he_so_xem_lai=2)['cps']
    print(f'Giá token và tỉ lệ xem lại cùng gấp đôi: {cps_cap:,.0f} đ ({cps_cap / cps_goc - 1:+.1%})')
    xep_hang = sorted(tac_dong_theo_yeu_to.items(), key=lambda muc: muc[1], reverse=True)
    for hang, (yeu_to, tac_dong) in enumerate(xep_hang[:3], start=1):
        print(f'{hang}. {yeu_to}: {tac_dong:.1%}')

    print('\nB3 · Chi phí khi giới hạn số lần chạy')
    print('Giới hạn | Tổng trợ lý (simulated) | Không thành công | Cả hệ thống (simulated) | CPS (simulated)')
    for lan, ket_qua in theo_gioi_han.items():
        khong_thanh_cong = len(reqs) - ket_qua['thanh_cong']
        chi_phi_he_thong = ket_qua['tong'] + BASELINE * khong_thanh_cong
        print(f"{lan} | {ket_qua['tong']:,.0f} đ | {khong_thanh_cong} | "
              f"{chi_phi_he_thong:,.0f} đ | {ket_qua['cps']:,.0f} đ")

    print('\nB4 · Xem lại 100% ca có kết quả ok trong noi_dia + hang_nang')
    reqs_co_run_ok = runs.loc[runs['status'].eq('ok'), 'request_id']
    can_xem_lai = reqs_pham_vi['request_id'].isin(reqs_co_run_ok)
    can_lam_lai = reqs_pham_vi['ket_qua'].eq('lam_lai')
    phut_lam_lai_trung_binh = reqs.loc[reqs['ket_qua'].eq('lam_lai'), 'phut_lam_lai_simulated'].mean()
    print(f'{can_xem_lai.sum()} ca xem lại, {can_lam_lai.sum()} ca làm lại, 5 phút/ca xem lại')
    for phut_lam_lai in (9, round(phut_lam_lai_trung_binh, 1)):
        reqs_xem_lai = reqs_pham_vi.assign(
            phut_xem_lai_simulated=5 * can_xem_lai,
            phut_lam_lai_simulated=phut_lam_lai * can_lam_lai,
        )
        ket_qua = mo_hinh(runs, reqs_xem_lai)
        ngan_sach_xem_lai = (
            BASELINE * ket_qua['thanh_cong'] - ket_qua['token'] - ket_qua['tool'] - ket_qua['lam_lai']
        )
        phut_xem_lai_hoa_von = ngan_sach_xem_lai / (can_xem_lai.sum() * LUONG_PHUT)
        print(f"Làm lại {phut_lam_lai:g} phút/ca: {ket_qua['cps']:,.0f} đ/việc "
              f"({ket_qua['cps'] / BASELINE:.2f}×), hòa vốn ở {phut_xem_lai_hoa_von:.1f} phút xem lại/ca (simulated)")


if __name__ == '__main__':
    # Giữ dấu tiếng Việt khi stdout dùng bảng mã cũ của Windows.
    if sys.stdout.encoding != 'utf-8':
        sys.stdout.reconfigure(encoding='utf-8')
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    print('\nA2 · Mô hình chi phí từ trace')
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        so_le = 2 if ten == 'hoa_don_moi_yc' else 0
        nhan = ' (simulated)' if ten in ('xem_lai', 'lam_lai', 'tong', 'cps') else ''
        print(f'{ten:16s} {gia_tri:>14,.{so_le}f}{nhan}')
    print(f"CPS / hoá đơn mỗi yêu cầu: {ket_qua['cps'] / ket_qua['hoa_don_moi_yc']:.1f}× (simulated)")
    print(f"Tỉ trọng chi phí làm lại: {ket_qua['lam_lai'] / ket_qua['tong']:.1%} (simulated)")

    print('\nA3 · Chi phí theo loại yêu cầu')
    print('Loại | Số yêu cầu | Thành công | Lần chạy/yêu cầu | CPS (simulated) | So với 12.000 đ (simulated)')
    for loai, reqs_loai in reqs.groupby('loai', sort=False):
        theo_loai = mo_hinh(runs, reqs_loai)
        ti_le = theo_loai['thanh_cong'] / len(reqs_loai)
        print(f"{loai} | {len(reqs_loai)} | {ti_le:.1%} | {reqs_loai['so_lan_chay'].mean():.2f} | "
              f"{theo_loai['cps']:,.0f} | {theo_loai['cps'] / BASELINE:.2f}×")

    runs_theo_loai = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    for loai, runs_loai in runs_theo_loai.groupby('loai', sort=False):
        ti_le_ok = runs_loai['status'].eq('ok').groupby(runs_loai['attempt']).mean()
        theo_lan = ', '.join(f'lần {lan}: {ti_le:.1%}' for lan, ti_le in ti_le_ok.items())
        print(f'Tỉ lệ ok của {loai}: {theo_lan}')

    print('\nA4 · Chi phí cố định cho noi_dia + hang_nang')
    reqs_pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    pham_vi = mo_hinh(runs, reqs_pham_vi)
    # Khối lượng tháng gồm mọi loại, nên dùng số thành công trong phạm vi trên toàn mẫu.
    ti_le_thanh_cong_pham_vi = pham_vi['thanh_cong'] / len(reqs)
    print('Yêu cầu/tháng | Thành công/tháng | Cố định/việc | CPS gồm cố định (simulated) | So với 12.000 đ (simulated)')
    for khoi_luong in (45_000, 22_500):
        viec_thanh_cong_thang = khoi_luong * ti_le_thanh_cong_pham_vi
        co_dinh_moi_viec = 40_000_000 / viec_thanh_cong_thang
        cps_gom_co_dinh = pham_vi['cps'] + co_dinh_moi_viec
        print(f'{khoi_luong:,} | {viec_thanh_cong_thang:,.0f} | {co_dinh_moi_viec:,.0f} | '
              f'{cps_gom_co_dinh:,.0f} | {cps_gom_co_dinh / BASELINE:.2f}×')

    in_bang_do_nhay(runs, reqs, ket_qua['cps'], reqs_pham_vi)
    # TODO CP4 · Nhiệm vụ D: cỡ mẫu.
    #   from statsmodels.stats.proportion import proportion_effectsize
    #   from statsmodels.stats.power import NormalIndPower
