Summary:	Switching tool for controlling "flip flop" USB devices
Summary(pl.UTF-8):	Narzędzie do sterowania przełączającymi się urządzeniami USB
Name:		usb-modeswitch
Version:	1.2.5
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://www.draisberghof.de/usb_modeswitch/%{name}-%{version}.tar.bz2
# Source0-md5:	c393603908eceab95444c5bde790f6f0
Patch0:		%{name}-makefile.patch
URL:		http://www.draisberghof.de/usb_modeswitch/
BuildRequires:	libusb-compat-devel >= 0.1
Requires:	tcl >= 8.4
Suggests:	usb-modeswitch-data
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
USB Modeswitch brings up your datacard into operational mode. When
plugged in they identify themselves as CD-ROM and present some
non-Linux compatible installation files. This tool deactivates this
cdrom-devices and enables the real communication device. It supports
most devices built and sold by Huawei, T-Mobile, Vodafone, Option,
ZTE, Novatel.

%description -l pl.UTF-8
USB Modeswitch potrafi przełączyć pewne urządzenia komunikacyjne w
tryb operacyjny. Takie urządzenia po podłączeniu identyfikują się jako
CD-ROM i oferują jedynie niezgodne z Linuksem pliki instalacyjne. To
narzędzie wyłącza emulację CD i włącza prawdziwe urządzenie
komunikacjne. Obsługuje większość urządzeń wytworzonych i oferowanych
przez firmy Huawei, T-Mobile, Vodafone, Option, ZTE, Novatel.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	CPPFLAGS="%{rpmcppflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_sbindir}/usb_modeswitch
%attr(755,root,root) %{_sbindir}/usb_modeswitch_dispatcher
%attr(755,root,root) /lib/udev/usb_modeswitch
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/usb_modeswitch.conf
%{_mandir}/man1/usb_modeswitch.1*
%dir /var/lib/usb_modeswitch
