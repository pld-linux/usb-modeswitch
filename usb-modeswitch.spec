Summary:	Switching tool for controlling "flip flop" USB devices
Summary(pl.UTF-8):	Narzędzie do sterowania przełączającymi się urządzeniami USB
Name:		usb-modeswitch
Version:	2.6.0
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://www.draisberghof.de/usb_modeswitch/%{name}-%{version}.tar.bz2
# Source0-md5:	be73dcc84025794081a1d4d4e5a75e4c
Patch0:		%{name}-makefile.patch
URL:		http://www.draisberghof.de/usb_modeswitch/
BuildRequires:	libusb-devel >= 1.0
BuildRequires:	pkgconfig
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
install -d $RPM_BUILD_ROOT/etc/usb_modeswitch.d

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -D usb_modeswitch@.service $RPM_BUILD_ROOT%{systemdunitdir}/usb_modeswitch@.service

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_sbindir}/usb_modeswitch
%attr(755,root,root) %{_sbindir}/usb_modeswitch_dispatcher
%attr(755,root,root) /lib/udev/usb_modeswitch
%{systemdunitdir}/usb_modeswitch@.service
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/usb_modeswitch.conf
%{_mandir}/man1/usb_modeswitch.1*
%{_mandir}/man1/usb_modeswitch_dispatcher.1*
%dir /etc/usb_modeswitch.d
%dir /var/lib/usb_modeswitch
