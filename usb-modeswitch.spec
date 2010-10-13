# TODO: Check if passing $(CPPFLAGS) to gcc is OK as done in patch0 ?
Summary:	Switching tool for controlling "flip flop" USB devices
Name:		usb-modeswitch
Version:	1.1.4
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://www.draisberghof.de/usb_modeswitch/%{name}-%{version}.tar.bz2
# Source0-md5:	a04db36bd0fc6fb303df7567f677b714
Patch0:		%{name}-makefile.patch
URL:		http://www.draisberghof.de/usb_modeswitch/
BuildRequires:	libusb-compat-devel
Requires:	tcl
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
# %%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	CPPFLAGS="%{rpmcppflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/usb_modeswitch.d

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README device_reference.txt
%attr(755,root,root) %{_sbindir}/usb_modeswitch
%attr(755,root,root) %{_sbindir}/usb_modeswitch_dispatcher
%attr(755,root,root) /lib/udev/usb_modeswitch
%dir %{_sysconfdir}/usb_modeswitch.d
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/usb_modeswitch.conf
%{_mandir}/man1/usb_modeswitch.1*
