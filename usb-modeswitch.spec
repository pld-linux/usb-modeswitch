Summary:	Switching tool for controlling "flip flop" USB devices
Name:		usb-modeswitch
Version:	1.1.8
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://www.draisberghof.de/usb_modeswitch/%{name}-%{version}.tar.bz2
# Source0-md5:	1aaaa45e0465843e4973d7778bfbafbb
Patch0:		%{name}-makefile.patch
URL:		http://www.draisberghof.de/usb_modeswitch/
BuildRequires:	libusb-compat-devel
Requires:	tcl >= 8.4
Suggests:	usb-modeswitch-data
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
USB Modeswitch brings up your datacard into operational mode. When
plugged in they identify themselves as cdrom and present some
non-Linux compatible installation files. This tool deactivates this
cdrom-devices and enables the real communication device. It supports
most devices built and sold by Huawei, T-Mobile, Vodafone, Option,
ZTE, Novatel.

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
