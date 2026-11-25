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
    if max_lan_chay is not None:
        raise NotImplementedError('Giới hạn số lần chạy thuộc CP2')

    runs = runs[runs['request_id'].isin(reqs['request_id'])]
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

    # TODO CP2 · Nhiệm vụ B: đổi từng yếu tố, ghi vào bảng độ nhạy.
    # TODO CP4 · Nhiệm vụ D: cỡ mẫu.
    #   from statsmodels.stats.proportion import proportion_effectsize
    #   from statsmodels.stats.power import NormalIndPower
